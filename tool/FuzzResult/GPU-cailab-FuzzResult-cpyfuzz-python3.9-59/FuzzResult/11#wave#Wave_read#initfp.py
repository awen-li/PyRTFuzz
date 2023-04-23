from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['BufferedReader']

def demoFunc(arg):
    try:
        obj = wave.Wave_read(None)
        file = PyDecode(API_TYPE_LIST, arg)
        obj.initfp(file)
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                PyCall_1682108932_BCUUl(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682108932_BCUUl(x):
    demoFunc(x)
