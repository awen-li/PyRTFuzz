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
            PyPrint(obj)
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682251146_GCGSV(x)

def PyCall_1682251146_amqbz(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)

def PyCall_1682251146_SCPWh(x):
    PyCall_1682251146_amqbz(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682251146_EVsln(x):
    PyCall_1682251146_SCPWh(x)

def PyCall_1682251146_GCGSV(x):
    with open('/dev/null', 'r'):
        PyCall_1682251146_EVsln(x)
