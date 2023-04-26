from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['BufferedWriter']

def demoFunc(arg):
    try:
        obj = wave.Wave_write(None)
        file = PyDecode(API_TYPE_LIST, arg)
        obj.initfp(file)
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    W_d1 = 0
    while (W_d1 in range(0, 1)):
        W_d1 += 1
        with open('/dev/null', 'r'):
            for F_X1 in range(0, 1):
                W_i1 = 0
                while (W_i1 in range(0, 1)):
                    W_i1 += 1
                    if True:
                        if True:
                            with open('/dev/null', 'r'):
                                demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
