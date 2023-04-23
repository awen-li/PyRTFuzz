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
            ret = obj.getcomptype()
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    if True:
        if True:
            with open('/dev/null', 'r'):
                if True:
                    PyCall_1682262926_PspYB(x)

def PyCall_1682262926_PspYB(x):
    if True:
        if True:
            with open('/dev/null', 'r'):
                if True:
                    dc = demoCls()
                    dc.demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
