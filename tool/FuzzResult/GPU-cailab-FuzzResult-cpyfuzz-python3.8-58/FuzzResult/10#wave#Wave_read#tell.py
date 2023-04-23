from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = wave.Wave_read(None)
            ret = obj.tell()
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682237245_KiUgl(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682237245_KiUgl(x):
    W_o1 = 0
    while (W_o1 in range(0, 1)):
        W_o1 += 1
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                for F_j1 in range(0, 1):
                    W_c1 = 0
                    while (W_c1 in range(0, 1)):
                        W_c1 += 1
                        for F_j1 in range(0, 1):
                            dc = demoCls()
                            dc.demoFunc(x)
