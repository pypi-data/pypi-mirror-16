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

import json
from subprocess import PIPE, Popen, call

from .base import PackageManager


class Homebrew(PackageManager):

    cli = '/usr/local/bin/brew'

    def sync(self):
        """ Fetch latest Homebrew formulas.

        Sample of brew output:

            $ brew outdated --json=v1
            [
              {
                "name": "cassandra",
                "installed_versions": [
                  "3.5"
                ],
                "current_version": "3.7"
              },
              {
                "name": "vim",
                "installed_versions": [
                  "7.4.1967"
                ],
                "current_version": "7.4.1993"
              },
              {
                "name": "youtube-dl",
                "installed_versions": [
                  "2016.07.06"
                ],
                "current_version": "2016.07.09.1"
              }
            ]
        """
        self.run(self.cli, 'update')

        # List available updates.
        output = self.run(self.cli, 'outdated', '--json=v1')
        if not output:
            return

        for pkg_info in json.loads(output):
            self.updates.append({
                'name': pkg_info['name'],
                # Only keeps the highest installed version.
                'installed_version': max(pkg_info['installed_versions']),
                'latest_version': pkg_info['current_version']})

    def update_cli(self, package_name=None):
        cmd = "{} upgrade --cleanup".format(self.cli)
        if package_name:
            cmd += " {}".format(package_name)
        return self.bitbar_cli_format(cmd)

    def update_all_cli(self):
        return self.update_cli()


class Cask(Homebrew):

    @property
    def active(self):
        """ Cask depends on vanilla Homebrew. """
        if super(Cask, self).active:
            cask = Popen([self.cli, 'cask'], stdout=PIPE, stderr=PIPE)
            cask.communicate()
            return cask.returncode == 0
        return False

    def sync(self):
        """ Fetch latest formulas and their metadata.

        Sample of brew cask output:

            $ brew cask list --versions
            aerial 1.2beta5, 1.1
            android-file-transfer latest
            audacity 2.1.2-1453294898, 2.1.2
            bitbar 1.9.1
            chromium latest
            firefox 47.0, 46.0.1, 46.0
            flux 37.3, 37.2, 37.1, 36.8, 36.6
            gimp 2.8.16-x86_64
            java 1.8.0_92-b14
            prey
            ubersicht

            $ brew cask info aerial
            aerial: 1.2beta5
            Aerial Screensaver
            https://github.com/JohnCoates/Aerial
            /usr/local/Caskroom/aerial/1.2beta5 (0B)
            https://github.com/caskroom/homebrew-cask/blob/master/Casks/aerial.rb
            ==> Contents
              Aerial.saver (screen_saver)

            $ brew cask info firefox
            firefox: 47.0.1
            Mozilla Firefox
            https://www.mozilla.org/en-US/firefox/
            Not installed
            https://github.com/caskroom/homebrew-cask/blob/master/Casks/firefox.rb
            ==> Contents
              Firefox.app (app)

            $ brew cask info prey
            prey: 1.5.1
            Prey
            https://preyproject.com
            Not installed
            https://github.com/caskroom/homebrew-cask/blob/master/Casks/prey.rb
            ==> Contents
              prey-mac-1.5.1-x86.pkg (pkg)

            $ brew cask info ubersicht
            ubersicht: 1.0.42
            Übersicht
            http://tracesof.net/uebersicht
            Not installed
            https://github.com/caskroom/homebrew-cask/blob/master/Casks/ubersicht.rb
            ==> Contents
              Übersicht.app (app)
        """
        # `brew cask update` is just an alias to `brew update`. Perform the
        # action anyway to make it future proof.
        self.run(self.cli, 'cask', 'update')

        # List installed packages.
        output = self.run(self.cli, 'cask', 'list', '--versions')

        # Inspect package one by one as `brew cask list` is not reliable. See:
        # https://github.com/caskroom/homebrew-cask/blob/master/doc
        # /reporting_bugs/brew_cask_list_shows_wrong_information.md
        for installed_pkg in output.strip().split('\n'):
            if not installed_pkg:
                continue
            name, versions = installed_pkg.split(' ', 1)

            # Use heuristics to guess installed version.
            versions = sorted([
                v.strip() for v in versions.split(',') if v.strip()])
            if len(versions) > 1 and 'latest' in versions:
                versions.remove('latest')
            version = versions[-1] if versions else '?'

            # TODO: Support packages removed from repository (reported with a
            # `(!)` flag). See: https://github.com/caskroom/homebrew-cask/blob
            # /master/doc/reporting_bugs
            # /uninstall_wrongly_reports_cask_as_not_installed.md

            # Inspect the package closer to evaluate its state.
            output = self.run(self.cli, 'cask', 'info', name)

            # Consider package as up-to-date if installed.
            if output.find('Not installed') == -1:
                continue

            latest_version = output.split('\n')[0].split(' ')[1]

            self.updates.append({
                'name': name,
                'installed_version': version,
                'latest_version': latest_version})

    def update_cli(self, package_name):
        """ Install a package.

        TODO: wait for https://github.com/caskroom/homebrew-cask/issues/22647
        so we can force a cleanup in one go, as we do above with vanilla
        Homebrew.
        """
        return self.bitbar_cli_format(
            "{} cask install {}".format(self.cli, package_name))

    def update_all_cli(self):
        """ Cask has no way to update all outdated packages.

        See: https://github.com/caskroom/homebrew-cask/issues/4678
        """
        return self.bitbar_cli_format(self._update_all_cmd())

    def update_all_cmd(self):
        self.sync()
        for package in self.updates:
            call("{} cask install {}".format(self.cli, package['name']),
                 shell=True)
