from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = sunau.Au_read(None)
            id = PyDecode(API_TYPE_LIST, arg)
            obj.getmark(id)
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682125817_PTGgY(x)

def PyCall_1682125817_PNfcW(x):
    dc = demoCls()
    dc.demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682125817_zTsHd(x):
    with open('/dev/null', 'r'):
        PyCall_1682125817_PNfcW(x)

def PyCall_1682125817_PTGgY(x):
    PyCall_1682125817_zTsHd(x)
