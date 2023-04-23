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
            obj = wave.Wave_write(None)
            ret = obj.getframerate()
            PyPrint(obj)
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682199938_zULDS(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682199938_Yjzvy(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            for F_I1 in range(0, 1):
                W_t1 = 0
                while (W_t1 in range(0, 1)):
                    W_t1 += 1
                    W_D1 = 0
                    while (W_D1 in range(0, 1)):
                        W_D1 += 1
                        dc = demoCls()
                        dc.demoFunc(x)

def PyCall_1682199938_zULDS(x):
    W_Z1 = 0
    while (W_Z1 in range(0, 1)):
        W_Z1 += 1
        PyCall_1682199938_Yjzvy(x)
