from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = aifc.Aifc_read(None)
        ret = obj.getmarkers()
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    W_E1 = 0
    while (W_E1 in range(0, 1)):
        W_E1 += 1
        W_O1 = 0
        while (W_O1 in range(0, 1)):
            W_O1 += 1
            for F_m1 in range(0, 1):
                PyCall_1682112205_IRqsr(x)

def PyCall_1682112205_bejFx(x):
    W_T1 = 0
    while (W_T1 in range(0, 1)):
        W_T1 += 1
        for F_v1 in range(0, 1):
            demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682112205_IRqsr(x):
    if True:
        with open('/dev/null', 'r'):
            W_c1 = 0
            while (W_c1 in range(0, 1)):
                W_c1 += 1
                PyCall_1682112205_bejFx(x)
