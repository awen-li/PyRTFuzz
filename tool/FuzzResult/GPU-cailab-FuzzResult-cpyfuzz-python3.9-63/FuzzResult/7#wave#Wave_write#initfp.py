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
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        if True:
            PyCall_1682235253_SeoJF(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682235253_SeoJF(x):
    with open('/dev/null', 'r'):
        if True:
            dc = demoCls()
            dc.demoFunc(x)
