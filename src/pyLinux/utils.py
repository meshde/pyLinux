import errno
import os
import ctypes

def is_type(var, typ):
    return isinstance(var, typ)

def is_root():
    import os
    return os.geteuid() == 0

def get_object_from_pointer(pointer):
    return ctypes.cast(pointer, ctypes.py_object).value

def is_alive(pid):
    try:
        os.kill(pid, 0)
    except OSError as err:
        if err.errno == errno.ESRCH:
            return False
        if err.errno == errno.EPERM:
            return True
        raise err
    return True
