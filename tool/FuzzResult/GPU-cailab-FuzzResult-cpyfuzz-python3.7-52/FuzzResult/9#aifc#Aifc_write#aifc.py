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
            obj.aifc()
            PyPrint(obj)
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682100493_msqvh(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682100493_fxmeg(x):
    with open('/dev/null', 'r'):
        if True:
            if True:
                with open('/dev/null', 'r'):
                    dc = demoCls()
                    dc.demoFunc(x)

def PyCall_1682100493_msqvh(x):
    PyCall_1682100493_fxmeg(x)
