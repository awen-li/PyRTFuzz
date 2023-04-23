from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['BufferedReader']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = wave.Wave_read(None)
            file = PyDecode(API_TYPE_LIST, arg)
            obj.initfp(file)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682158245_CalCk(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682158245_XvvoL(x):
    with open('/dev/null', 'r'):
        if True:
            dc = demoCls()
            dc.demoFunc(x)

def PyCall_1682158245_CalCk(x):
    PyCall_1682158245_XvvoL(x)
