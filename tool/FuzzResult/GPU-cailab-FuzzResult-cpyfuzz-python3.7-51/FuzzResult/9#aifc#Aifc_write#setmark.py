from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int', 'int', 'bytes']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = aifc.Aifc_write(None)
            (id, pos, name) = PyDecode(API_TYPE_LIST, arg)
            obj.setmark(id, pos, name)
            PyPrint(obj)
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    if True:
        if True:
            if True:
                PyCall_1682220687_BJsVV(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682220687_BJsVV(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
