#!/usr/bin/env python
#
# test_vmdktool.py - Unit test cases for COT.helpers.vmdktoolsubmodule.
#
# March 2015, Glenn F. Matthews
# Copyright (c) 2014-2016 the COT project developers.
# See the COPYRIGHT.txt file at the top-level directory of this distribution
# and at https://github.com/glennmatthews/cot/blob/master/COPYRIGHT.txt.
#
# This file is part of the Common OVF Tool (COT) project.
# It is subject to the license terms in the LICENSE.txt file found in the
# top-level directory of this distribution and at
# https://github.com/glennmatthews/cot/blob/master/LICENSE.txt. No part
# of COT, including this file, may be copied, modified, propagated, or
# distributed except according to the terms contained in the LICENSE.txt file.

"""Unit test cases for the COT.helpers.vmdktool submodule."""

import os
from distutils.version import StrictVersion

import mock

from COT.helpers.tests.test_helper import HelperUT
from COT.helpers.vmdktool import VmdkTool


class TestVmdkTool(HelperUT):
    """Test cases for VmdkTool helper class."""

    def setUp(self):
        """Test case setup function called automatically prior to each test."""
        self.helper = VmdkTool()
        super(TestVmdkTool, self).setUp()

    def test_get_version(self):
        """Test .version getter logic."""
        self.fake_output = "vmdktool version 1.4"
        self.assertEqual(StrictVersion("1.4"), self.helper.version)

    def test_install_helper_already_present(self):
        """Do nothing instead of re-installing."""
        self.helper.install_helper()
        self.assertEqual([], self.last_argv)
        self.assertLogged(**self.ALREADY_INSTALLED)

    @mock.patch('os.path.isdir')
    @mock.patch('os.path.exists')
    @mock.patch('os.makedirs')
    def test_install_helper_apt_get(self,
                                    mock_makedirs,
                                    mock_exists,
                                    mock_isdir):
        """Test installation via 'apt-get'."""
        mock_isdir.return_value = False
        mock_exists.return_value = False
        mock_makedirs.side_effect = OSError
        self.enable_apt_install()
        self.helper.install_helper()
        self.assertEqual([
            ['dpkg', '-s', 'make'],
            ['apt-get', '-q', 'update'],
            ['apt-get', '-q', 'install', 'make'],
            ['dpkg', '-s', 'zlib1g-dev'],
            ['apt-get', '-q', 'install', 'zlib1g-dev'],
            ['make', 'CFLAGS="-D_GNU_SOURCE -g -O -pipe"'],
            ['sudo', 'mkdir', '-p', '--mode=755', '/usr/local/man/man8'],
            ['sudo', 'mkdir', '-p', '--mode=755', '/usr/local/bin'],
            ['make', 'install', 'PREFIX=/usr/local'],
        ], self.last_argv)
        self.assertAptUpdated()
        # Make sure we don't 'apt-get update/install' again unnecessarily
        self.fake_output = 'install ok installed'
        os.environ['PREFIX'] = '/opt/local'
        os.environ['DESTDIR'] = '/home/cot'
        self.last_argv = []
        self.helper.install_helper()
        self.assertEqual([
            ['dpkg', '-s', 'make'],
            ['dpkg', '-s', 'zlib1g-dev'],
            ['make', 'CFLAGS="-D_GNU_SOURCE -g -O -pipe"'],
            ['sudo', 'mkdir', '-p', '--mode=755',
             '/home/cot/opt/local/man/man8'],
            ['sudo', 'mkdir', '-p', '--mode=755', '/home/cot/opt/local/bin'],
            ['make', 'install', 'PREFIX=/opt/local', 'DESTDIR=/home/cot'],
        ], self.last_argv)

    def test_install_helper_port(self):
        """Test installation via 'port'."""
        self.port_install_test('vmdktool')

    @mock.patch('os.path.isdir')
    @mock.patch('os.path.exists')
    @mock.patch('os.makedirs')
    def test_install_helper_yum(self,
                                mock_makedirs,
                                mock_exists,
                                mock_isdir):
        """Test installation via 'yum'."""
        mock_isdir.return_value = False
        mock_exists.return_value = False
        mock_makedirs.side_effect = OSError
        self.enable_yum_install()
        self.helper.install_helper()
        self.assertEqual([
            ['yum', '--quiet', 'install', 'make'],
            ['yum', '--quiet', 'install', 'zlib-devel'],
            ['make', 'CFLAGS="-D_GNU_SOURCE -g -O -pipe"'],
            ['sudo', 'mkdir', '-p', '--mode=755', '/usr/local/man/man8'],
            ['sudo', 'mkdir', '-p', '--mode=755', '/usr/local/bin'],
            ['make', 'install', 'PREFIX=/usr/local'],
        ], self.last_argv)

    def test_install_helper_unsupported(self):
        """Unable to install without a package manager."""
        self.select_package_manager(None)
        with self.assertRaises(NotImplementedError):
            self.helper.install_helper()

    def test_convert_unsupported(self):
        """Negative test - conversion to unsupported format/subformat."""
        with self.assertRaises(NotImplementedError):
            self.helper.convert_disk_image(self.blank_vmdk, self.temp_dir,
                                           'qcow2')
        with self.assertRaises(NotImplementedError):
            self.helper.convert_disk_image(self.blank_vmdk, self.temp_dir,
                                           'vmdk', 'monolithicSparse')
