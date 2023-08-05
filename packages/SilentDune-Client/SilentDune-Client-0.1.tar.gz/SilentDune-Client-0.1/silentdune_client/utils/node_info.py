#
# Authors: Robert Abram <robert.abram@entpack.com>
#
# Copyright (C) 2015-2016 EntPack
# see file 'LICENSE' for use and warranty information
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import logging
import os
import random
import string
import sys
from subprocess import check_output, CalledProcessError

from silentdune_client.utils.console import ConsoleBase
from silentdune_client.utils.misc import \
    which, determine_config_root, get_active_firewall, get_init_system, is_service_running

_logger = logging.getLogger('sd-client')


class NodeInformation(ConsoleBase):

    # External programs
    ps = None
    pgrep = None
    sed = None
    kill = None
    tail = None

    # ipv4 commands
    iptables_exec = None
    iptables_save = None
    iptables_restore = None

    # ipv6 commands
    ip6tables_exec = None
    ip6tables_save = None
    ip6tables_restore = None

    # Configuration Items
    root_user = (os.getuid() == 0)
    config_root = None
    machine_id = None
    pid_file = None
    log_file = None

    # Upstart
    ups_installed = False

    # Systemd
    sysd_installed = False

    # sysvinit
    sysv_installed = False

    # Previous firewall service
    previous_firewall_service = None

    # Firewall_platform - Currently only iptables is supported.
    firewall_platform = 'iptables'

    # OS Platform - IE: linux, osx, ...
    platform = 'linux'

    error = False

    def __init__(self, silent=False):
        """
        Gather all the information we need about this node.
        """
        self.silent = silent

        try:

            if sys.platform == "linux" or sys.platform == "linux2":
                self.platform = 'linux'
            elif sys.platform == "darwin":
                self.platform = 'osx'  # OS X
            elif sys.platform == "win32":
                self.platform = 'windows'

            self.cwrite('Determining configuration root path...')

            # Gather information about this node.
            self.config_root = determine_config_root()
            if not self.config_root:
                self.error = True
                self.cwriteline('[Error]', 'Unable to determine configuration root.')
                return

            self.cwriteline('[OK]', 'Configuration root set to "{0}"'.format(self.config_root))

            # Check to see if our configuration path is in a home directory.
            if os.path.expanduser('~') in self.config_root:
                _logger.warning('Not running as root, setting configuration path to "{0}"'.format(self.config_root))
                _logger.warning('Since we are not running as root, system firewall settings will not be changed.')

            # Change the default path for pid and log file to config_root.
            self.pid_file = os.path.join(self.config_root, 'sdc.pid')
            self.log_file = os.path.join(self.config_root, 'sdc.log')

            if not self._check_for_external_progs():
                self.error = True
            elif not self._init_system_check():
                self.error = True
            elif not self._firewall_check():
                self.error = True
            elif not self._get_machine_id():
                self.error = True

        except:
            self.error = True

    def _which_wrapper(self, name):
        """
        If program is not found, set an error.
        :param name: Program name
        :return: Program path or None
        """

        p = which(name)
        if not p:
            _logger.debug('Failed to find program path for "{0}"'.format(name))
            self.error = True

        return p

    def _check_for_external_progs(self):
        """
        Find external programs used by this client.
        """

        # Use _which_wrapper to set an error for any missing programs.
        self.ps = self._which_wrapper('ps')
        self.pgrep = self._which_wrapper('pgrep')
        self.sed = self._which_wrapper('sed')
        self.kill = self._which_wrapper('kill')
        self.tail = self._which_wrapper('tail')

        self.iptables_exec = self._which_wrapper('iptables')
        self.iptables_save = self._which_wrapper('iptables-save')
        self.iptables_restore = self._which_wrapper('iptables-restore')

        self.ip6tables_exec = self._which_wrapper('ip6tables')
        self.ip6tables_save = self._which_wrapper('ip6tables-save')
        self.ip6tables_restore = self._which_wrapper('ip6tables-restore')

        if self.ps is None or self.pgrep is None:
            _logger.critical('Unable to determine which services are running on this machine.')
            return False

        if self.sed is None or self.kill is None or self.tail is None:
            _logger.critical('Missing system critical system executables.')

        if self.iptables_exec is None or self.iptables_save is None or self.iptables_restore is None:
            _logger.critical('Unable to find iptables executables.')
            return False

        return True

    def _init_system_check(self):
        """
        Determine which init system is running on this system.
        """

        self.cwrite('Determining Init system...  ')

        init = get_init_system()

        # If we didn't detect the init system, abort.
        if not init:
            self.cwriteline('[Error]', 'Unable to determine init system on this node.')
            return False

        if init == 'upstart':
            self.ups_installed = True
            self.cwriteline('[OK]', 'Detected Upstart based init system.')

        if init == 'systemd':
            self.sysd_installed = True
            self.cwriteline('[OK]', 'Detected Systemd based init system.')

        if init == 'sysv':
            self.sysv_installed = True
            self.cwriteline('[OK]', 'Detected sysvinit based init system.')

        return True

    def _firewall_check(self):
        """
        Get the currently running firewall service
        """

        self.cwrite('Checking for running firewall service...  ')

        self.previous_firewall_service = get_active_firewall()

        if not self.previous_firewall_service:
            self.cwriteline('[OK]', 'Unable to detect running firewall service.')
            return True

        self.cwriteline('[OK]', 'Detected {0} firewall service.'.format(self.previous_firewall_service))

        if not is_service_running(self.previous_firewall_service):
            _logger.info('{0} firewall service is not currently running.'.format(self.previous_firewall_service))

        return True

    def _get_machine_id(self):
        """
        Find the machine unique identifier or generate one for this machine.
        """

        m_id = None
        f = os.path.join(self.config_root, 'machine-id')

        _logger.debug('Looking up the machine-id value.')

        # See if we have an exiting machine-id file in our config root
        if os.path.exists(f):
            with open(f, 'r') as handle:
                m_id = handle.readline().strip('\n')

        if not m_id:

            # See if we can find a machine-id file on this machine
            for p in ['/etc/machine-id', '/var/lib/dbus/machine-id']:
                if os.path.isfile(p):
                    with open(p) as handle:
                        m_id = handle.readline().strip('\n')

        # If we can't find an existing machine id, make one up.
        if not m_id:
            _logger.debug('Existing machine_id not found.')
            m_id = self._write_machine_id()

        self.machine_id = m_id

        return True

    def _write_machine_id(self):
        """
        Create a new unique machine id for this node.
        """
        _logger.debug('Creating unique machine-id value.')

        m_id = ''.join(random.choice('abcdef' + string.digits) for _ in range(32))

        with open(os.path.join(self.config_root, 'machine-id'), 'w') as h:
            h.write(m_id + '\n')

        return m_id

    def _run_service_command(self, cmd, name):
        """
        Helper function for running system service commands.
        """
        # SysV and Upstart default
        prog = which('service')
        args = [prog, name, cmd]  # Note order of 'name' and 'cmd'

        # SystemD
        if self.sysd_installed:
            prog = which('systemctl')
            args = [prog, cmd, name]  # Note order of 'name' and 'cmd'

        try:
            check_output(args)
            return True
        except CalledProcessError:
            _logger.error('Program "{0} {1}" did not run successfully.'.format(prog, args))

        return False

    def start_service(self, name):
        """
        Start a system service.
        :param name: Name of service
        :return: True if successful, otherwise False
        """
        return self._run_service_command('start', name)

    def stop_service(self, name):
        """
        Stop a system service.
        :param name: Name of service
        :return: True if successful, otherwise False
        """
        return self._run_service_command('stop', name)

    def disable_service(self, name):
        """
        Disable a system service.
        :param name: Name of service
        :return: True if successful, otherwise False
        """
        # Sys V
        if self.sysv_installed:
            return self._run_service_command('disable', name)

        # System D mask service
        if self.sysd_installed:
            if not self._run_service_command('disable', name):
                return False
            return self._run_service_command('mask', name)

        if self.ups_installed:
            # Upstart requires an override file to disable the service
            try:
                with open('/etc/init/{0}.override'.format(name), 'w') as h:
                    h.write('manual')
                return True
            except IOError:
                _logger.error('Unable to create upstart service override file.')

        return False

    def enable_service(self, name):
        """
        Enable a system service.
        :param name: Name of service
        :return: True if successful, otherwise False
        """
        # Sys V
        if self.sysv_installed:
            return self._run_service_command('enable', name)

        # SystemD service
        if self.sysd_installed:
            self._run_service_command('unmask', name)
            return self._run_service_command('enable', name)

        # Upstart service
        if self.ups_installed:

            file = '/etc/init/{0}.override'.format(name)
            # Check to see if the override file exists.
            if os.path.exists(file):
                os.remove(file)
            else:
                try:
                    check_output([self.sed, "-i '/manual/d' '/etc/init/{0}'".format(name)])
                    return True
                except CalledProcessError:
                    _logger.error('Enabling upstart service failed.')

        return False

    def is_service_running(self, name):
        """
        Check to see if the given service is running.
        :param name: Name of service
        :return: True if service is running, otherwise False
        """
        # Sys V
        if self.sysv_installed:
            try:
                output = check_output('service {0} status | grep running', shell=True)
                if 'running' in output:
                    return True
                return False
            except CalledProcessError:
                return False

        # SystemD service
        if self.sysd_installed:
            try:
                output = check_output('systemctl status {0} | grep running', shell=True)
                if 'running' in output:
                    return True
                return False
            except CalledProcessError:
                return False

        # Upstart service
        if self.ups_installed:
            try:
                output = check_output('service {0} status | grep running', shell=True)
                if 'running' in output:
                    return True
                return False
            except CalledProcessError:
                return False

        return False
