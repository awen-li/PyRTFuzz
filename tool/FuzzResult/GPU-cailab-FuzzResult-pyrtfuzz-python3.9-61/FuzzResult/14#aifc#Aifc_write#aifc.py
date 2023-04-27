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
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    for F_C1 in range(0, 1):
        PyCall_1682431087_zHMar(x)

def PyCall_1682431086_BxLrw(x):
    if True:
        dc = demoCls()
        dc.demoFunc(x)

def PyCall_1682431086_tJVbz(x):
    for F_O1 in range(0, 1):
        PyCall_1682431086_BxLrw(x)

def PyCall_1682431086_EenGZ(x):
    PyCall_1682431086_tJVbz(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682431087_kUCbq(x):
    if True:
        for F_N1 in range(0, 1):
            PyCall_1682431086_EenGZ(x)

def PyCall_1682431087_zHMar(x):
    with open('/dev/null', 'r'):
        PyCall_1682431087_kUCbq(x)
