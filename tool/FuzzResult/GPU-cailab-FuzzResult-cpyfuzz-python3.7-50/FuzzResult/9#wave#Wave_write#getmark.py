from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = wave.Wave_write(None)
            id = PyDecode(API_TYPE_LIST, arg)
            obj.getmark(id)
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682173599_TPdhv(x)

def PyCall_1682173599_sCDRH(x):
    if True:
        dc = demoCls()
        dc.demoFunc(x)

def PyCall_1682173599_CMWtv(x):
    if True:
        PyCall_1682173599_sCDRH(x)

def PyCall_1682173599_TPdhv(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            PyCall_1682173599_CMWtv(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
