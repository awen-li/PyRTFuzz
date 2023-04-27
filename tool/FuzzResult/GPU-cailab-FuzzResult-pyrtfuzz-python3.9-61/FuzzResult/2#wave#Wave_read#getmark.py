from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['None']

def demoFunc(arg):
    try:
        obj = wave.Wave_read(None)
        id = PyDecode(API_TYPE_LIST, arg)
        obj.getmark(id)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    if True:
        with open('/dev/null', 'r'):
            demoFunc(x)
