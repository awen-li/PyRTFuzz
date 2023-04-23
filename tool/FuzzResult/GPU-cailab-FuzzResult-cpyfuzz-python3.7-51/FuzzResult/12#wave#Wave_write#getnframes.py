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
            ret = obj.getnframes()
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682105663_AdYnc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682105663_DtpPa(x):
    with open('/dev/null', 'r'):
        if True:
            for F_s1 in range(0, 1):
                for F_e1 in range(0, 1):
                    dc = demoCls()
                    dc.demoFunc(x)

def PyCall_1682105663_ELYnl(x):
    PyCall_1682105663_DtpPa(x)

def PyCall_1682105663_zHPfg(x):
    PyCall_1682105663_ELYnl(x)

def PyCall_1682105663_AdYnc(x):
    for F_W1 in range(0, 1):
        for F_h1 in range(0, 1):
            PyCall_1682105663_zHPfg(x)
