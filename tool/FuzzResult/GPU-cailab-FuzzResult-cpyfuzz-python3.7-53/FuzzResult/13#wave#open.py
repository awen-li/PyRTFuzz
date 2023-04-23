from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

API_TYPE_LIST = ['BytesIO', 'str']

def demoFunc(arg):
    try:
        (f, mode) = PyDecode(API_TYPE_LIST, arg)
        ret = wave.open(f, mode)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        PyCall_1682184227_DIMgn(x)

def PyCall_1682184227_lRMUn(x):
    demoFunc(x)

def PyCall_1682184227_jzkte(x):
    if True:
        if True:
            PyCall_1682184227_lRMUn(x)

def PyCall_1682184227_DIMgn(x):
    with open('/dev/null', 'r'):
        if True:
            if True:
                PyCall_1682184227_jzkte(x)
