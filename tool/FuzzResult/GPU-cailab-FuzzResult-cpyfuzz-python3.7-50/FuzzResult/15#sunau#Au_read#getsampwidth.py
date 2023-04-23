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
            ret = obj.getsampwidth()
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    if True:
        with open('/dev/null', 'r'):
            PyCall_1682142768_FParW(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682142768_OzGhw(x):
    if True:
        if True:
            dc = demoCls()
            dc.demoFunc(x)

def PyCall_1682142768_FParW(x):
    PyCall_1682142768_OzGhw(x)
