# Copyright 2015, 2016 IBM Corp.
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_log import log as logging
import retrying

from pypowervm import const as pvm_const
from pypowervm.utils import transaction as pvm_tx
from pypowervm.wrappers import base_partition as pvm_bp
from pypowervm.wrappers import managed_system as pvm_ms
from pypowervm.wrappers import virtual_io_server as pvm_vios

from nova_powervm import conf as cfg
from nova_powervm.virt.powervm import exception as nova_pvm_exc
from nova_powervm.virt.powervm.i18n import _LW

LOG = logging.getLogger(__name__)
CONF = cfg.CONF

# RMC must be either active or busy.  Busy is allowed because that simply
# means that something is running against the VIOS at the moment...but
# it should recover shortly.
VALID_RMC_STATES = [pvm_bp.RMCState.ACTIVE, pvm_bp.RMCState.BUSY]

# Only a running state is OK for now.
VALID_VM_STATES = [pvm_bp.LPARState.RUNNING]


def get_active_vioses(adapter, host_uuid, xag=None, vios_wraps=None):
    """Returns a list of active Virtual I/O Server Wrappers for a host.

    Active is defined by powered on and RMC state being 'active'.

    :param adapter: The pypowervm adapter for the query.
    :param host_uuid: The host server's UUID (not used).
    :param xag: (Optional, Default: None) List of extended attributes to use.
    :param vios_wraps: (Optional, Default: None) A list of VIOS wrappers. If
                       specified, the method will check for active VIOSes
                       in this list instead of issuing a GET.
    :return: List of VIOS wrappers.
    """
    if not vios_wraps:
        vios_wraps = pvm_vios.VIOS.get(adapter, xag=xag)

    return [vio for vio in vios_wraps if is_vios_active(vio)]


def get_inactive_running_vioses(vios_wraps):
    """Method to get RMC inactive but powered on VIOSes

    Not waiting for VIOS RMC states to go active when the host boots up
    may result in stale adapter mappings from evacuated instances.

    :param vios_wraps: A list of VIOS wrappers.
    :return: List of RMC inactive but powered on VIOSes from the list.
    """
    inactive_running_vioses = []
    for vios in vios_wraps:
        if (vios.rmc_state not in VALID_RMC_STATES and
           vios.state not in [pvm_bp.LPARState.NOT_ACTIVATED,
                              pvm_bp.LPARState.ERROR,
                              pvm_bp.LPARState.NOT_AVAILBLE,
                              pvm_bp.LPARState.SHUTTING_DOWN,
                              pvm_bp.LPARState.SUSPENDED,
                              pvm_bp.LPARState.SUSPENDING,
                              pvm_bp.LPARState.UNKNOWN]):
            inactive_running_vioses.append(vios)

    return inactive_running_vioses


def is_vios_active(vios):
    """Returns a boolean to indicate if the VIOS is active.

    Active is defined by running, and the RMC being 'active'.
    :param vios: The Virtual I/O Server wrapper to validate.
    :return: Boolean
    """
    return (vios.rmc_state in VALID_RMC_STATES and
            vios.state in VALID_VM_STATES)


def get_physical_wwpns(adapter, ms_uuid):
    """Returns the active WWPNs of the FC ports across all VIOSes on system."""
    resp = adapter.read(pvm_ms.System.schema_type, root_id=ms_uuid,
                        child_type=pvm_vios.VIOS.schema_type,
                        xag=[pvm_const.XAG.VIO_STOR])
    vios_feed = pvm_vios.VIOS.wrap(resp)
    wwpn_list = []
    for vios in vios_feed:
        wwpn_list.extend(vios.get_active_pfc_wwpns())
    return wwpn_list


def build_tx_feed_task(adapter, host_uuid, name='vio_feed_mgr',
                       xag=[pvm_const.XAG.VIO_STOR,
                            pvm_const.XAG.VIO_SMAP,
                            pvm_const.XAG.VIO_FMAP]):
    """Builds the pypowervm transaction FeedTask.

    The transaction FeedTask enables users to collect a set of
    'WrapperTasks' against a feed of entities (in this case a set of VIOSes).
    The WrapperTask (within the FeedTask) handles lock and retry.

    This is useful to batch together a set of updates across a feed of elements
    (and multiple updates within a given wrapper).  This allows for significant
    performance improvements.

    :param adapter: The pypowervm adapter for the query.
    :param host_uuid: The host server's UUID.
    :param name: (Optional) The name of the feed manager.  Defaults to
                 vio_feed_mgr.
    :param xag: (Optional) List of extended attributes to use.  If not passed
                in defaults to all storage options (as this is most common
                case for using a transaction manager).
    """

    active_vio_feed = get_active_vioses(adapter, host_uuid, xag=xag)
    if not active_vio_feed:
        raise nova_pvm_exc.NoActiveViosForFeedTask()

    return pvm_tx.FeedTask(name, active_vio_feed)


def validate_vios_ready(adapter, host_uuid):
    """Check whether VIOS rmc is up and running on this host.

    Will query the VIOSes for a period of time attempting to ensure all
    running VIOSes get an active RMC. If no VIOSes are ready by the timeout
    it will raise an exception. If only some of the VIOSes had RMC go active
    by the end of the wait period host initialization will continue.

    The timeout is defined by the vios_active_wait_timeout conf option.

    :param adapter: The pypowervm adapter for the query.
    :param host_uuid: The host server's UUID.
    :raises: A ViosNotAvailable exception if a VIOS is not available by a
             given timeout.
    """
    max_wait_time = CONF.powervm.vios_active_wait_timeout

    # Used to keep track of VIOSes and reduce queries to API
    vios_wraps = []
    rmc_down_vioses = []

    @retrying.retry(retry_on_result=lambda result: len(result) > 0,
                    wait_fixed=5 * 1000,
                    stop_max_delay=max_wait_time * 1000)
    def _wait_for_active_vioses():
        try:
            # Update the wrappers list and get the list of inactive
            # running VIOSes
            del vios_wraps[:]
            vios_wraps.extend(pvm_vios.VIOS.get(adapter))
            return get_inactive_running_vioses(vios_wraps)
        except Exception as e:
            LOG.exception(e)
            # If we errored then we want to keep retrying so return something
            # with a length greater than zero
            return [None]

    try:
        rmc_down_vioses = _wait_for_active_vioses()
    except retrying.RetryError:
        # This is thrown if we've hit our max retry count.  If so, no
        # issue... just continue
        pass

    if len(rmc_down_vioses) > 0 and rmc_down_vioses != [None]:
        LOG.warning(
            _LW('Timed out waiting for the RMC state of all the powered '
                'on Virtual I/O Servers to be active. Wait time was: '
                '%(time)s seconds. VIOSes that did not go active were: '
                '%(vioses)s.'),
            {'time': max_wait_time,
             'vioses': ', '.join([
                 vio.name for vio in rmc_down_vioses if vio is not None])})

    # If we didn't get a single active VIOS then raise an exception
    if not get_active_vioses(adapter, host_uuid, vios_wraps=vios_wraps):
        raise nova_pvm_exc.ViosNotAvailable(wait_time=max_wait_time)
