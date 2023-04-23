from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        obj = wave.Wave_read(None)
        pos = PyDecode(API_TYPE_LIST, arg)
        obj.setpos(pos)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    if True:
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                if True:
                    PyCall_1682147239_NmmKj(x)

def PyCall_1682147239_NmmKj(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                for F_G1 in range(0, 1):
                    if True:
                        W_I1 = 0
                        while (W_I1 in range(0, 1)):
                            W_I1 += 1
                            demoFunc(x)
