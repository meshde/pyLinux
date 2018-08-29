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

def test_unshare_mount(tmpdir):
    import os
    from pyLinux import linux

    def path_in_mounts(path):
        with open('/proc/mounts', 'r') as f:
            for line in f:
                line = line.strip()
                if path in line:
                    return True
        return False

    path = os.path.join(str(tmpdir), 'meshde')
    os.makedirs(path)

    r, w = os.pipe()

    pid = os.fork()

    if pid == 0:
        os.close(r)
        w = os.fdopen(w, 'w')

        linux.unshare(linux.CLONE_NEWNS)
        linux.mount(None, '/', None, linux.MS_PRIVATE | linux.MS_REC, None)
        linux.mount('tmpfs', path, 'tmpfs')
        assert path_in_mounts(path)

        w.write('I\'m done')
        w.close()

    else:
        os.close(w)
        r = os.fdopen(r)
        msg = r.read()
        print('Child sent:', msg)
        assert not path_in_mounts(path)

    return

def test_unshare_net():
    import os
    from pyLinux import linux

    pid = os.fork()

    if pid == 0:
        linux.unshare(linux.CLONE_NEWNET)

