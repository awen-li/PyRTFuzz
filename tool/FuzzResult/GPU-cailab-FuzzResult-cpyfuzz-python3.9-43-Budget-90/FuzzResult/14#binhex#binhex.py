from fuzzwrap import PyDecode 
from binhex import *
import binhex
import binascii
import io

API_TYPE_LIST = ['str', 'str']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (inp, out) = PyDecode(API_TYPE_LIST, arg)
            binhex.binhex(inp, out)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, binascii.Incomplete, binhex.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682173367_Qhvdt(x)

def PyCall_1682173367_EpVpX(x):
    if True:
        for F_x1 in range(0, 1):
            for F_f1 in range(0, 1):
                for F_S1 in range(0, 1):
                    for F_I1 in range(0, 1):
                        dc = demoCls()
                        dc.demoFunc(x)

def PyCall_1682173367_eBhQp(x):
    PyCall_1682173367_EpVpX(x)

def PyCall_1682173367_FPuqP(x):
    with open('/dev/null', 'r'):
        for F_Z1 in range(0, 1):
            PyCall_1682173367_eBhQp(x)

def PyCall_1682173367_Qhvdt(x):
    if True:
        for F_L1 in range(0, 1):
            PyCall_1682173367_FPuqP(x)
