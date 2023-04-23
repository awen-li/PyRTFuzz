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
            ret = obj.getmarkers()
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682126495_lyQPJ(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682126495_lyQPJ(x):
    with open('/dev/null', 'r'):
        for F_W1 in range(0, 1):
            for F_e1 in range(0, 1):
                if True:
                    dc = demoCls()
                    dc.demoFunc(x)
