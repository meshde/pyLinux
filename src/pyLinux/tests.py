def test_clone():
    import linux
    import os
    import time
    import utils

    def callback():
        print("here")
        print(os.getpid())
        time.sleep(10)
        return 0

    pid = linux.clone(callback)

    assert utils.is_alive(pid)
    status = linux.waitpid(pid)
    assert not utils.is_alive(pid)
    print('{} exited with status {}'.format(pid, status))
    return

def test_clone_args():
    import linux
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

def test_mount(tmpdir):
    import linux
    import os

    proc = str(tmpdir.mkdir('proc'))
    tmp = str(tmpdir.mkdir('tmp'))
    syspath = str(tmpdir.mkdir('sys'))

    assert linux.mount('proc', proc, 'proc') == 0
    assert linux.mount('tmpfs', tmp, 'tmpfs') == 0
    assert linux.mount('sysfs', syspath, 'sysfs') == 0

    # assert proc == ''

    assert os.listdir(proc) == os.listdir('/proc')
    assert os.listdir(syspath) == os.listdir('/sys')
    return
