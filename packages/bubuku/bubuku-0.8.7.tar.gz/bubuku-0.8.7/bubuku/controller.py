import logging
from time import sleep, time

from kazoo.exceptions import NodeExistsError

from bubuku.amazon import Amazon
from bubuku.broker import BrokerManager
from bubuku.zookeeper import Exhibitor

_LOG = logging.getLogger('bubuku.controller')


class Change(object):
    def get_name(self) -> str:
        raise NotImplementedError('Not implemented yet')

    def can_run(self, current_actions) -> bool:
        raise NotImplementedError('Not implemented yet')

    def run(self, current_actions) -> bool:
        raise NotImplementedError('Not implemented')

    def can_run_at_exit(self) -> bool:
        return False


class Check(object):
    def __init__(self, check_interval_s=5):
        self.check_interval_s = check_interval_s
        self.__last_check_timestamp_s = 0

    def check_if_time(self) -> Change:
        if self.time_till_check() <= 0:
            self.__last_check_timestamp_s = time()
            return self.check()
        return None

    def time_till_check(self):
        return self.__last_check_timestamp_s + self.check_interval_s - time()

    def check(self) -> Change:
        raise NotImplementedError('Not implemented')


def _exclude_self(ip, name, running_actions):
    return [k for k, v in running_actions.items() if k != name and v != ip]


class Controller(object):
    def __init__(self, broker_manager: BrokerManager, zk: Exhibitor, amazon: Amazon):
        self.broker_manager = broker_manager
        self.zk = zk
        self.amazon = amazon
        self.checks = []
        self.changes = {}  # Holds mapping from change name to array of pending changes
        self.running = True

    def add_check(self, check):
        _LOG.info('Adding check {}'.format(str(check)))
        self.checks.append(check)

    def _register_running_changes(self, ip: str) -> dict:
        _LOG.debug('Taking lock for processing')
        with self.zk.take_lock('/bubuku/global_lock', ip):
            _LOG.debug('Lock is taken')
            # Get list of current running changes
            running_changes = {
                change: self.zk.get('/bubuku/changes/{}'.format(change))[0].decode('utf-8')
                for change in self.zk.get_children('/bubuku/changes')
                }
            if running_changes:
                _LOG.info("Running changes: {}".format(running_changes))
            # Register changes to run
            for name, change_list in self.changes.items():
                # Only first change is able to run
                first_change = change_list[0]
                if first_change.can_run(_exclude_self(ip, name, running_changes)):
                    if name not in running_changes:
                        _LOG.info('Registering change in zk: {}'.format(name))
                        self.zk.create('/bubuku/changes/{}'.format(name), ip.encode('utf-8'), ephemeral=True)
                        running_changes[name] = ip
                else:
                    _LOG.info('Change {} is waiting for others: {}'.format(name, running_changes))
            return running_changes

    def _run_changes(self, running_changes: dict, ip: str) -> list:
        changes_to_remove = []
        for name, change_list in self.changes.items():
            if name in running_changes and running_changes[name] == ip:
                change = change_list[0]
                _LOG.info('Executing action {} step'.format(change))
                if self.running or change.can_run_at_exit():
                    if not change.run(_exclude_self(ip, change.get_name(), running_changes)):
                        _LOG.info('Action {} completed'.format(change))
                        changes_to_remove.append(change.get_name())
                    else:
                        _LOG.info('Action {} will be executed on next loop step'.format(change))
                else:
                    _LOG.info(
                        'Action {} can not be run while stopping, forcing to stop it'.format(change))
                    changes_to_remove.append(change.get_name())
        return changes_to_remove

    def _release_changes_lock(self, changes_to_remove):
        if changes_to_remove:
            for change_name in changes_to_remove:
                del self.changes[change_name][0]
                if not self.changes[change_name]:
                    del self.changes[change_name]
            with self.zk.take_lock('/bubuku/global_lock'):
                for name in changes_to_remove:
                    _LOG.info('Removing action {} from locks'.format(name))
                    self.zk.delete('/bubuku/changes/{}'.format(name), recursive=True)

    def loop(self):
        ip = self.amazon.get_own_ip()

        try:
            self.zk.create('/bubuku/changes', makepath=True)
        except NodeExistsError:
            pass
        while self.running or self.changes:
            self.make_step(ip)

            if self.changes:
                sleep(0.5)
            else:
                min_time_till_check = min([check.time_till_check() for check in self.checks])
                if min_time_till_check > 0:
                    sleep(min_time_till_check)

    def make_step(self, ip):
        # register running changes
        running_changes = self._register_running_changes(ip)
        # apply changes without holding lock
        changes_to_remove = self._run_changes(running_changes, ip)
        # remove processed actions
        self._release_changes_lock(changes_to_remove)
        if self.running:
            for check in self.checks:
                _LOG.info('Executing check {}'.format(check))
                self._add_change_to_queue(check.check_if_time())

    def _add_change_to_queue(self, change):
        if not change:
            return
        _LOG.info('Adding change {} to pending changes'.format(change.get_name()))
        if change.get_name() not in self.changes:
            self.changes[change.get_name()] = []
        self.changes[change.get_name()].append(change)

    def stop(self, change: Change):
        _LOG.info('Stopping controller with additional change: {}'.format(change.get_name() if change else None))
        # clear all pending changes
        self._add_change_to_queue(change)
        self.running = False
