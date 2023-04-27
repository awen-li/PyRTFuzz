from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['BufferedWriter']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = wave.Wave_write(None)
            file = PyDecode(API_TYPE_LIST, arg)
            obj.initfp(file)
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        PyCall_1682328031_NRQOw(x)

def PyCall_1682328031_uNkUc(x):
    if True:
        dc = demoCls()
        dc.demoFunc(x)

def PyCall_1682328031_NRQOw(x):
    PyCall_1682328031_uNkUc(x)
