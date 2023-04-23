from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = wave.Wave_write(None)
        ret = obj.getsampwidth()
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682259658_JoiBp(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682259658_JoiBp(x):
    if True:
        with open('/dev/null', 'r'):
            if True:
                if True:
                    demoFunc(x)
