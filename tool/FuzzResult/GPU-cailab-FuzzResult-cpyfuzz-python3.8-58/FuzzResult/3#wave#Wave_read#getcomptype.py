from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = wave.Wave_read(None)
        ret = obj.getcomptype()
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        PyCall_1682177054_qiWcj(x)

def PyCall_1682177054_qiWcj(x):
    with open('/dev/null', 'r'):
        demoFunc(x)
