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
            ret = obj.getnchannels()
            PyPrint(obj)
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
            pass

def RunFuzzer(x):
    for F_x1 in range(0, 1):
        with open('/dev/null', 'r'):
            if True:
                with open('/dev/null', 'r'):
                    with open('/dev/null', 'r'):
                        if True:
                            W_y1 = 0
                            while (W_y1 in range(0, 1)):
                                W_y1 += 1
                                dc = demoCls()
                                dc.demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
