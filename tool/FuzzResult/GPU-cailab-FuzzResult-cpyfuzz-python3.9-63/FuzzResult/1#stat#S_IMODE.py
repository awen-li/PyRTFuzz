from fuzzwrap import PyDecode 
from stat import *
import stat

API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        mode = PyDecode(API_TYPE_LIST, arg)
        ret = stat.S_IMODE(mode)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    PyCall_1681347994_aorhv(x)

def PyCall_1681347994_aorhv(x):
    demoFunc(x)
