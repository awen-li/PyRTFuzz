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
            ret = obj.tell()
            PyPrint(obj)
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    if True:
        with open('/dev/null', 'r'):
            PyCall_1682153926_dptnA(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682153926_dptnA(x):
    if True:
        if True:
            with open('/dev/null', 'r'):
                with open('/dev/null', 'r'):
                    dc = demoCls()
                    dc.demoFunc(x)
