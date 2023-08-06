import logging

from bubuku.broker import BrokerManager
from bubuku.controller import Change, Check
from bubuku.zookeeper import Exhibitor

_LOG = logging.getLogger('bubuku.features.restart_on_zk')

_STAGE_STOP = 'stop'
_STAGE_CHECK_LEADERSHIP = 'check_leader'
_STAGE_START = 'start'


class RestartBrokerOnZkChange(Change):
    def __init__(self, zk_hosts: str, zk: Exhibitor, broker: BrokerManager):
        self.conn_str = zk_hosts
        self.zk = zk
        self.broker = broker
        self.stage = _STAGE_STOP

    def get_name(self):
        return 'restart'

    def can_run(self, current_actions):
        return all([a not in current_actions for a in ['start', 'restart', 'stop']])

    def run(self, current_actions):
        if self.stage == _STAGE_STOP:
            current_conn_str = self.zk.get_conn_str()
            if current_conn_str != self.conn_str:
                _LOG.warning('ZK address changed again, from {} to {}'.format(self.conn_str, current_conn_str))
                return False
            self.broker.stop_kafka_process()
            self.stage = _STAGE_CHECK_LEADERSHIP
            return True
        elif self.stage == _STAGE_CHECK_LEADERSHIP:
            if not self.broker.has_leadership():
                self.stage = _STAGE_START
            return True
        elif self.stage == _STAGE_START:
            # Yep, use latest data
            self.broker.start_kafka_process(self.zk.get_conn_str())
            return False
        else:
            _LOG.error('Stage {} is not supported'.format(self.stage))
        return False

    def __str__(self):
        return 'RestartOnZkChange ({}), stage={}, new_conn_str={}'.format(self.get_name(), self.stage, self.conn_str)


class CheckExhibitorAddressChanged(Check):
    def __init__(self, zk: Exhibitor, broker: BrokerManager):
        super().__init__()
        self.zk = zk
        self.broker = broker
        self.conn_str = None

    def check(self) -> Change:
        new_conn_str = self.zk.get_conn_str()
        if new_conn_str != self.conn_str:
            _LOG.info('ZK addresses changed from {} to {}, triggering restart'.format(self.conn_str, new_conn_str))
            self.conn_str = new_conn_str
            return RestartBrokerOnZkChange(new_conn_str, self.zk, self.broker)

    def __str__(self):
        return 'CheckExhibitorAddressChanged, current={}'.format(self.conn_str)
