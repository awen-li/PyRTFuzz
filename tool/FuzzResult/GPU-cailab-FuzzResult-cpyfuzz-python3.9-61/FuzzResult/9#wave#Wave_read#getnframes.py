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
            ret = obj.getnframes()
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
            pass

def RunFuzzer(x):
    if True:
        PyCall_1682260461_IxvKA(x)

def PyCall_1682260461_pHPeR(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            dc = demoCls()
            dc.demoFunc(x)

def PyCall_1682260461_lNJxW(x):
    if True:
        PyCall_1682260461_pHPeR(x)

def PyCall_1682260461_IxvKA(x):
    if True:
        with open('/dev/null', 'r'):
            PyCall_1682260461_lNJxW(x)
