# -*- coding: utf-8 -*-
"""Unit tests of pyLinux"""

import sys
from nose.tools import nottest, istest
from nose.tools import set_trace  # Breakpoint for nosetests
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

import resources


###
# Test layers
###

@nottest
def setUpModule():
    sys.path.append('../src/')
    # Setups for all tests of this module
    return

@nottest
def tearDownModule():
    # Cleanups for all tests of this module
    return

###
# Test cases
###

class LinuxTest(unittest.TestCase):
    """ Tests for the linux module """
    @classmethod
    def setUpClass(cls):
        return

    @classmethod
    def tearDownClass(cls):
        return

    def setUp(self):
        import os
        self.tmpdir = os.path.join('~', 'nose/')
        os.makedirs(self.tmpdir)
        return

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmpdir)
        del self.tmpdir
        return

    def test_clone(self):
        from pyLinux import linux
        import os
        import time

        def callback():
            print("here")
            print(os.getpid())
            time.sleep(10)
            return 0

        pid = linux.clone(callback)
        # print(pid)
        # print(type(pid))
        # _, status = os.waitpid(pid, 0)
        status = linux.waitpid(pid)
        print('{} exited with status {}'.format(pid, status))
        return

    def test_clone_args(self):
        from pyLinux import linux
        import ctypes

        def callback(val):
            # phrase = ctypes.c_char_p.from_buffer(val)
            print('Hello')
            print(val)
            valu = ctypes.cast(val, ctypes.py_object)
            print('Value is:', valu.value)
            print('Types is:', type(valu))
            return 0

        pid = linux.clone(callback, args=['Mehmood'])
        status = linux.waitpid(pid)
        print('{} exited with status {}'.format(pid, status))
        return

    def test_mount(self):
        from pyLinux import linux
        import os

        proc = os.path.join(self.tmpdir, 'proc')
        tmp = os.path.join(self.tmpdir, 'tmp')
        syspath = os.path.join(self.tmpdir, 'sys')

        for x in (proc, tmp, syspath):
            os.makedirs(x)

        assert linux.mount('proc', proc, 'proc') == 0
        assert linux.mount('tmpfs', tmp, 'tmpfs') == 0
        assert linux.mount('sysfs', syspath, 'sysfs') == 0

        # assert proc == ''

        assert os.listdir(proc) == os.listdir('/proc')
        assert os.listdir(syspath) == os.listdir('/sys')

        assert linux.umount(proc) == 0
        assert linux.umount(tmp) == 0
        assert linux.umount(syspath) == 0

        return


class CgroupsTest(unittest.TestCase):
    """ Tests for the cgroups module """
    @classmethod
    def setUpClass(cls):
        from pyLinux.cgroups import Cgroup
        global Cgroup
        # Setups before first test of this class
        return

    @classmethod
    def tearDownClass(cls):
        # Cleanups after last test of this class
        return

    def setUp(self):
        # Setups before each test of this class
        return

    def tearDown(self):
        # Cleanups after each test of this class
        return

    def test_files_exist(self):
        import os
        cgroup = Cgroup('meshde')
        resource = 'cpu'
        attribute = 'cpu.shares'
        value = 2
        cgroup.set(resource, attribute, value)

        cgroup_dir = cgroup.get_cgroup_dir(resource)
        cpu_dir = os.path.join(Cgroup.BASEDIR, resource)

        assert cgroup.assigned(resource)

        attribute_path = os.path.join(cgroup_dir, attribute)
        with open(attribute_path, 'r') as f:
            lines = f.readlines()
            assert len(lines) == 1
            line = lines[0].strip()
            val = int(line)

            assert value == val
        return
