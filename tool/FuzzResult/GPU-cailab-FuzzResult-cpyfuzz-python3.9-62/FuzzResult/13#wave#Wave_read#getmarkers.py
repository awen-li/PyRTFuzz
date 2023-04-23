from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = wave.Wave_read(None)
            ret = obj.getmarkers()
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
            pass

def RunFuzzer(x):
    if True:
        if True:
            PyCall_1682203386_iktWZ(x)

def PyCall_1682203386_GMIHX(x):
    dc = demoCls()
    dc.demoFunc(x)

def PyCall_1682203386_iktWZ(x):
    if True:
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                if True:
                    if True:
                        PyCall_1682203386_GMIHX(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
