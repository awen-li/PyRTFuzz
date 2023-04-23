from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = wave.Wave_write(None)
        ret = obj.getcomptype()
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    W_L1 = 0
    while (W_L1 in range(0, 1)):
        W_L1 += 1
        for F_t1 in range(0, 1):
            with open('/dev/null', 'r'):
                for F_N1 in range(0, 1):
                    PyCall_1682257011_zJJZw(x)

def PyCall_1682257011_GzysH(x):
    demoFunc(x)

def PyCall_1682257011_Zgeuq(x):
    with open('/dev/null', 'r'):
        if True:
            PyCall_1682257011_GzysH(x)

def PyCall_1682257011_zJJZw(x):
    PyCall_1682257011_Zgeuq(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
