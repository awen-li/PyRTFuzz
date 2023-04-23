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
            obj = aifc.Aifc_read(None)
            ret = obj.getmarkers()
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        PyCall_1682253817_rvGLA(x)

def PyCall_1682253817_CmFGU(x):
    dc = demoCls()
    dc.demoFunc(x)

def PyCall_1682253817_qDqjY(x):
    PyCall_1682253817_CmFGU(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682253817_cwMmj(x):
    with open('/dev/null', 'r'):
        PyCall_1682253817_qDqjY(x)

def PyCall_1682253817_mHEFk(x):
    PyCall_1682253817_cwMmj(x)

def PyCall_1682253817_rvGLA(x):
    PyCall_1682253817_mHEFk(x)
