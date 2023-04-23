from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

API_TYPE_LIST = ['BytesIO', 'str']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (f, mode) = PyDecode(API_TYPE_LIST, arg)
            ret = wave.open(f, mode)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)
