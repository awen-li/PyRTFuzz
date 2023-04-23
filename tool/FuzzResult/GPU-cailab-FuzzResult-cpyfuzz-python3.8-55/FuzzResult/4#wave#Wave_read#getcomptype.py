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
            ret = obj.getcomptype()
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
            pass

def RunFuzzer(x):
    W_p1 = 0
    while (W_p1 in range(0, 1)):
        W_p1 += 1
        with open('/dev/null', 'r'):
            PyCall_1682100696_aeFMv(x)

def PyCall_1682100696_aeFMv(x):
    dc = demoCls()
    dc.demoFunc(x)
