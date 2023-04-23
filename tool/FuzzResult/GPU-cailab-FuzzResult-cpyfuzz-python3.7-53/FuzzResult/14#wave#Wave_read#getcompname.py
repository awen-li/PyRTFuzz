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
            ret = obj.getcompname()
            PyPrint(obj)
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
            pass

def RunFuzzer(x):
    W_p1 = 0
    while (W_p1 in range(0, 1)):
        W_p1 += 1
        with open('/dev/null', 'r'):
            PyCall_1682138874_wrzpi(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682138874_GINhg(x):
    W_E1 = 0
    while (W_E1 in range(0, 1)):
        W_E1 += 1
        dc = demoCls()
        dc.demoFunc(x)

def PyCall_1682138874_wrzpi(x):
    if True:
        W_a1 = 0
        while (W_a1 in range(0, 1)):
            W_a1 += 1
            W_p1 = 0
            while (W_p1 in range(0, 1)):
                W_p1 += 1
                PyCall_1682138874_GINhg(x)
