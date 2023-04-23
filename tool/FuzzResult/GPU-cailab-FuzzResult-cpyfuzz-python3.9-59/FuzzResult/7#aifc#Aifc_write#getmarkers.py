from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = aifc.Aifc_write(None)
            ret = obj.getmarkers()
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682238373_wYExB(x)

def PyCall_1682238373_AKZzT(x):
    dc = demoCls()
    dc.demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682238373_wYExB(x):
    if True:
        with open('/dev/null', 'r'):
            PyCall_1682238373_AKZzT(x)
