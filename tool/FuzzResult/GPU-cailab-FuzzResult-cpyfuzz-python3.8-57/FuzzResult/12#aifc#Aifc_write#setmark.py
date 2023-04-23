from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int', 'int', 'bytes']

def demoFunc(arg):
    try:
        obj = aifc.Aifc_write(None)
        (id, pos, name) = PyDecode(API_TYPE_LIST, arg)
        obj.setmark(id, pos, name)
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682156389_cbiDu(x)

def PyCall_1682156389_bOruH(x):
    with open('/dev/null', 'r'):
        demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682156389_uMIRf(x):
    for F_u1 in range(0, 1):
        with open('/dev/null', 'r'):
            W_j1 = 0
            while (W_j1 in range(0, 1)):
                W_j1 += 1
                PyCall_1682156389_bOruH(x)

def PyCall_1682156389_cbiDu(x):
    if True:
        if True:
            PyCall_1682156389_uMIRf(x)
