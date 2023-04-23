from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = wave.Wave_read(None)
        ret = obj.getcompname()
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682243121_mlgIY(x)

def PyCall_1682243121_mlgIY(x):
    W_E1 = 0
    while (W_E1 in range(0, 1)):
        W_E1 += 1
        if True:
            with open('/dev/null', 'r'):
                demoFunc(x)
