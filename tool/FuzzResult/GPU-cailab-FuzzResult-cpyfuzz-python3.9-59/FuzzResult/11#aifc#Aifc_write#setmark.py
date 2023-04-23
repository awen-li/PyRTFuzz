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
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            if True:
                PyCall_1682168127_Rvgma(x)

def PyCall_1682168127_HNVLQ(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)

def PyCall_1682168127_bewzR(x):
    PyCall_1682168127_HNVLQ(x)

def PyCall_1682168127_yvZtm(x):
    PyCall_1682168127_bewzR(x)

def PyCall_1682168127_Rvgma(x):
    PyCall_1682168127_yvZtm(x)
