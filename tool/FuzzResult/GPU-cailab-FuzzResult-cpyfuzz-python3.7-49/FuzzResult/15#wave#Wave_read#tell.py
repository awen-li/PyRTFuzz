from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = wave.Wave_read(None)
        ret = obj.tell()
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        PyCall_1682118143_DmQsz(x)

def PyCall_1682118143_KtHdd(x):
    demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682118143_uUaON(x):
    if True:
        with open('/dev/null', 'r'):
            if True:
                PyCall_1682118143_KtHdd(x)

def PyCall_1682118143_DmQsz(x):
    if True:
        PyCall_1682118143_uUaON(x)
