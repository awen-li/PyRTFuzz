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
            ret = obj.getparams()
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682219149_amOja(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682219149_dhSEK(x):
    if True:
        dc = demoCls()
        dc.demoFunc(x)

def PyCall_1682219149_amOja(x):
    with open('/dev/null', 'r'):
        PyCall_1682219149_dhSEK(x)
