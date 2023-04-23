from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

API_TYPE_LIST = ['str', 'str']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (f, mode) = PyDecode(API_TYPE_LIST, arg)
            ret = aifc.openfp(f, mode)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682176102_jxSxO(x)

def PyCall_1682176101_raFXi(x):
    if True:
        if True:
            dc = demoCls()
            dc.demoFunc(x)

def PyCall_1682176102_tfsoD(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            PyCall_1682176101_raFXi(x)

def PyCall_1682176102_jxSxO(x):
    PyCall_1682176102_tfsoD(x)
