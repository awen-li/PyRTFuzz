from fuzzwrap import PyDecode 
from stat import *
import stat

API_TYPE_LIST = ['int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            mode = PyDecode(API_TYPE_LIST, arg)
            ret = stat.S_IMODE(mode)
        except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)
