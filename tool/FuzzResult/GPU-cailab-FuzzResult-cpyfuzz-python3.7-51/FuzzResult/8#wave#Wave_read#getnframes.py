from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = wave.Wave_read(None)
        ret = obj.getnframes()
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        if True:
            W_f1 = 0
            while (W_f1 in range(0, 1)):
                W_f1 += 1
                W_G1 = 0
                while (W_G1 in range(0, 1)):
                    W_G1 += 1
                    if True:
                        with open('/dev/null', 'r'):
                            with open('/dev/null', 'r'):
                                demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
