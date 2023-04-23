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
            obj = wave.Wave_write(None)
            ret = obj.getcomptype()
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
            pass

def RunFuzzer(x):
    if True:
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                PyCall_1682250191_ijQOt(x)

def PyCall_1682250191_ijQOt(x):
    dc = demoCls()
    dc.demoFunc(x)
