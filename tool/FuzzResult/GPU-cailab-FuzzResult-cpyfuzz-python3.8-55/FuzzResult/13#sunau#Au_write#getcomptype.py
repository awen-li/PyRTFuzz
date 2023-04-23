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
            obj = sunau.Au_write(None)
            ret = obj.getcomptype()
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682251825_VzNtC(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682251825_bjrSd(x):
    if True:
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                with open('/dev/null', 'r'):
                    dc = demoCls()
                    dc.demoFunc(x)

def PyCall_1682251825_MFpAF(x):
    PyCall_1682251825_bjrSd(x)

def PyCall_1682251825_VzNtC(x):
    PyCall_1682251825_MFpAF(x)
