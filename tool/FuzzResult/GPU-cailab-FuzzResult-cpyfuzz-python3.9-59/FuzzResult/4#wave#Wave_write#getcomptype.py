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
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682118538_GMeDI(x)

def PyCall_1682118538_GMeDI(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            W_M1 = 0
            while (W_M1 in range(0, 1)):
                W_M1 += 1
                demoFunc(x)
