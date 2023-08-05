#!/usr/bin/env python
#
# fatdisk.py - Unit test cases for COT.helpers.fatdisk submodule.
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

"""Unit test cases for the COT.helpers.fatdisk module."""

import logging
import os
import re
from distutils.version import StrictVersion

import mock

from COT.helpers.tests.test_helper import HelperUT
from COT.helpers.helper import Helper
from COT.helpers.fatdisk import FatDisk

logger = logging.getLogger(__name__)


class TestFatDisk(HelperUT):
    """Test cases for FatDisk helper class."""

    def setUp(self):
        """Test case setup function called automatically prior to each test."""
        self.helper = FatDisk()
        super(TestFatDisk, self).setUp()

    def test_get_version(self):
        """Validate .version getter."""
        self.fake_output = "fatdisk, version 1.0.0-beta"
        self.assertEqual(StrictVersion("1.0.0"), self.helper.version)

    def test_install_helper_already_present(self):
        """Trying to re-install is a no-op."""
        self.helper.install_helper()
        self.assertEqual([], self.last_argv)
        self.assertLogged(**self.ALREADY_INSTALLED)

    @mock.patch('shutil.copy')
    @mock.patch('os.path.isdir')
    @mock.patch('os.path.exists')
    @mock.patch('os.makedirs')
    def test_install_helper_apt_get(self,
                                    mock_makedirs,
                                    mock_exists,
                                    mock_isdir,
                                    mock_copy):
        """Test installation via 'apt-get'."""
        mock_isdir.return_value = False
        mock_exists.return_value = False
        mock_makedirs.side_effect = OSError
        mock_copy.return_value = True
        self.enable_apt_install()
        self.helper.install_helper()
        self.assertEqual([
            ['dpkg', '-s', 'make'],
            ['apt-get', '-q', 'update'],
            ['apt-get', '-q', 'install', 'make'],
            ['dpkg', '-s', 'gcc'],
            ['apt-get', '-q', 'install', 'gcc'],
            ['./RUNME'],
            ['sudo', 'mkdir', '-p', '--mode=755', '/usr/local/bin'],
        ], self.last_argv)
        self.assertTrue(re.search("/fatdisk$", mock_copy.call_args[0][0]))
        self.assertEqual('/usr/local/bin', mock_copy.call_args[0][1])
        self.assertAptUpdated()
        # Make sure we don't call apt-get update/install again unnecessarily.
        self.last_argv = []
        self.fake_output = 'install ok installed'
        os.environ['PREFIX'] = '/opt/local'
        os.environ['DESTDIR'] = '/home/cot'
        self.helper.install_helper()
        self.assertEqual([
            ['dpkg', '-s', 'make'],
            ['dpkg', '-s', 'gcc'],
            ['./RUNME'],
            ['sudo', 'mkdir', '-p', '--mode=755', '/home/cot/opt/local/bin'],
        ], self.last_argv)
        self.assertTrue(re.search("/fatdisk$", mock_copy.call_args[0][0]))
        self.assertEqual('/home/cot/opt/local/bin', mock_copy.call_args[0][1])

    def test_install_helper_port(self):
        """Test installation via 'port'."""
        self.port_install_test('fatdisk')

    @mock.patch('shutil.copy')
    @mock.patch('os.path.isdir')
    @mock.patch('os.path.exists')
    @mock.patch('os.makedirs')
    def test_install_helper_yum(self,
                                mock_makedirs,
                                mock_exists,
                                mock_isdir,
                                mock_copy):
        """Test installation via 'yum'."""
        mock_isdir.return_value = False
        mock_exists.return_value = False
        mock_makedirs.side_effect = OSError
        mock_copy.return_value = True
        self.enable_yum_install()
        self.helper.install_helper()
        self.assertEqual([
            ['yum', '--quiet', 'install', 'make'],
            ['yum', '--quiet', 'install', 'gcc'],
            ['./RUNME'],
            ['sudo', 'mkdir', '-p', '--mode=755', '/usr/local/bin'],
        ], self.last_argv)
        self.assertTrue(re.search("/fatdisk$", mock_copy.call_args[0][0]))
        self.assertEqual('/usr/local/bin', mock_copy.call_args[0][1])

    def test_install_helper_linux_need_make_no_package_manager(self):
        """Linux installation requires yum or apt-get if 'make' missing."""
        self.select_package_manager(None)
        self.system = 'Linux'
        with self.assertRaises(NotImplementedError):
            self.helper.install_helper()

    def test_install_helper_linux_need_compiler_no_package_manager(self):
        """Linux installation requires yum or apt-get if 'gcc' missing."""
        self.select_package_manager(None)

        def new_stub_find_executable(_, name):
            """Stub for Helper.find_executable - returns a fixed response."""
            logger.info("stub_find_executable(%s)", name)
            if name == 'make':
                return "/bin/make"
            else:
                return None
        Helper.find_executable = new_stub_find_executable
        self.system = 'Linux'
        with self.assertRaises(NotImplementedError):
            self.helper.install_helper()

    def test_install_helper_unsupported(self):
        """No support for installation under Windows."""
        self.select_package_manager(None)
        self.system = 'Windows'
        with self.assertRaises(NotImplementedError):
            self.helper.install_helper()
