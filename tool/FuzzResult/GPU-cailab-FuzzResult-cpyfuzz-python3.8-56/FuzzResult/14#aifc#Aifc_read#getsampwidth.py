from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = aifc.Aifc_read(None)
        ret = obj.getsampwidth()
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    for F_K1 in range(0, 1):
        if True:
            PyCall_1682170173_uPIvL(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682170173_iiLvw(x):
    W_d1 = 0
    while (W_d1 in range(0, 1)):
        W_d1 += 1
        with open('/dev/null', 'r'):
            demoFunc(x)

def PyCall_1682170173_uPIvL(x):
    for F_i1 in range(0, 1):
        for F_f1 in range(0, 1):
            PyCall_1682170173_iiLvw(x)
