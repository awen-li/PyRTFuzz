from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        obj = wave.Wave_read(None)
        nframes = PyDecode(API_TYPE_LIST, arg)
        ret = obj.readframes(nframes)
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    if True:
        if True:
            W_l1 = 0
            while (W_l1 in range(0, 1)):
                W_l1 += 1
                W_o1 = 0
                while (W_o1 in range(0, 1)):
                    W_o1 += 1
                    for F_s1 in range(0, 1):
                        with open('/dev/null', 'r'):
                            PyCall_1682143943_RxOQy(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682143943_RxOQy(x):
    W_J1 = 0
    while (W_J1 in range(0, 1)):
        W_J1 += 1
        for F_T1 in range(0, 1):
            if True:
                demoFunc(x)
