from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = sunau.Au_read(None)
            ret = obj.getnframes()
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    if True:
        PyCall_1682147739_AhkXb(x)

def PyCall_1682147739_iAoXS(x):
    if True:
        if True:
            with open('/dev/null', 'r'):
                if True:
                    dc = demoCls()
                    dc.demoFunc(x)

def PyCall_1682147739_AhkXb(x):
    PyCall_1682147739_iAoXS(x)
