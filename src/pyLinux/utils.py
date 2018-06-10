def is_type(var, typ):
    return isinstance(var, typ)

def is_root():
    import os
    return os.geteuid() == 0

def get_object_from_pointer(pointer):
    return ctypes.cast(pointer, ctypes.py_object).value
