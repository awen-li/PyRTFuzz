from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['BufferedWriter']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = sunau.Au_write(None)
            file = PyDecode(API_TYPE_LIST, arg)
            obj.initfp(file)
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    if True:
        PyCall_1682239963_wLHsD(x)

def PyCall_1682239963_vHiNW(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)

def PyCall_1682239963_wLHsD(x):
    PyCall_1682239963_vHiNW(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
