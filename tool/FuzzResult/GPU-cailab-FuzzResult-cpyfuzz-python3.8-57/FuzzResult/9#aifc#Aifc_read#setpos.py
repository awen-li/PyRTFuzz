from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = aifc.Aifc_read(None)
            pos = PyDecode(API_TYPE_LIST, arg)
            obj.setpos(pos)
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682258109_mvLUx(x)

def PyCall_1682258109_pFZCS(x):
    with open('/dev/null', 'r'):
        if True:
            dc = demoCls()
            dc.demoFunc(x)

def PyCall_1682258109_mvLUx(x):
    PyCall_1682258109_pFZCS(x)
