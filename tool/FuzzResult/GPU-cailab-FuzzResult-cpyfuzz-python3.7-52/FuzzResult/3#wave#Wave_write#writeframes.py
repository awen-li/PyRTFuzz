from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['bytes']

def demoFunc(arg):
    try:
        obj = wave.Wave_write(None)
        data = PyDecode(API_TYPE_LIST, arg)
        obj.writeframes(data)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        if True:
            demoFunc(x)
