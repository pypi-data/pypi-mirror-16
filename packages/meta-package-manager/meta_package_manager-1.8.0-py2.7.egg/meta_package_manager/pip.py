# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Kevin Deldycke <kevin@deldycke.com>
#                    and contributors.
# All Rights Reserved.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.


from __future__ import print_function, unicode_literals

import re

from .base import PackageManager


class Pip(PackageManager):

    def sync(self):
        """ List outdated packages and their metadata.

        Sample of pip output:

            $ pip list --outdated
            ccm (2.1.8, /Users/kdeldycke/ccm) - Latest: 2.1.11 [sdist]
            coverage (4.0.3) - Latest: 4.1 [wheel]
            IMAPClient (0.13) - Latest: 1.0.1 [wheel]
            Logbook (0.10.1) - Latest: 1.0.0 [sdist]
            mccabe (0.4.0) - Latest: 0.5.0 [wheel]
            mercurial (3.8.3) - Latest: 3.8.4 [sdist]
            pylint (1.5.6) - Latest: 1.6.1 [wheel]
        """
        output = self.run(self.cli, 'list', '--outdated').strip()
        if not output:
            return

        regexp = re.compile(r'(\S+) \((.*)\) - Latest: (\S+)')
        for outdated_pkg in output.split('\n'):
            if not outdated_pkg:
                continue

            name, installed_info, latest_version = regexp.match(
                outdated_pkg).groups()

            # Extract current non-standard location if found.
            installed_info = installed_info.split(',', 1)
            version = installed_info[0]
            special_location = " ({})".format(
                installed_info[1].strip()) if len(installed_info) > 1 else ''

            self.updates.append({
                'name': name + special_location,
                'installed_version': version,
                'latest_version': latest_version})

    def update_cli(self, package_name):
        return self.bitbar_cli_format(
            "{} install --upgrade {}".format(self.cli, package_name))

    def update_all_cli(self):
        """ Produce a long CLI with all upgradeable package names.

        This work around the lack of proper full upgrade command in Pip.
        See: https://github.com/pypa/pip/issues/59
        """
        return self.bitbar_cli_format(self._update_all_cmd())

    def update_all_cmd(self):
        self.sync()
        for package in self.updates:
            call("{} install -U {}".format(self.cli, package["name"]),
                 shell=True)


class Pip2(Pip):

    cli = '/usr/local/bin/pip2'

    @property
    def name(self):
        return "Python 2 pip"


class Pip3(Pip):

    cli = '/usr/local/bin/pip3'

    @property
    def name(self):
        return "Python 3 pip"
