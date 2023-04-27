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
            obj = wave.Wave_read(None)
            id = PyDecode(API_TYPE_LIST, arg)
            obj.getmark(id)
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682314811_EADwb(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682314811_xiDVm(x):
    with open('/dev/null', 'r'):
        W_l1 = 0
        while (W_l1 in range(0, 1)):
            W_l1 += 1
            with open('/dev/null', 'r'):
                dc = demoCls()
                dc.demoFunc(x)

def PyCall_1682314811_auqwb(x):
    with open('/dev/null', 'r'):
        for F_N1 in range(0, 1):
            with open('/dev/null', 'r'):
                PyCall_1682314811_xiDVm(x)

def PyCall_1682314811_EADwb(x):
    W_J1 = 0
    while (W_J1 in range(0, 1)):
        W_J1 += 1
        PyCall_1682314811_auqwb(x)
