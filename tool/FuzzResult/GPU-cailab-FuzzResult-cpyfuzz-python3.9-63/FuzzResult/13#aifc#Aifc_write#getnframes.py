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
            ret = obj.getnframes()
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        if True:
            if True:
                if True:
                    with open('/dev/null', 'r'):
                        with open('/dev/null', 'r'):
                            PyCall_1682194884_UmZRB(x)

def PyCall_1682194884_UmZRB(x):
    dc = demoCls()
    dc.demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
