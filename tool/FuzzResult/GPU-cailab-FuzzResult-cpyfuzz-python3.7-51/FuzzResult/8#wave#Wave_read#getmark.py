from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['None']

def demoFunc(arg):
    try:
        obj = wave.Wave_read(None)
        id = PyDecode(API_TYPE_LIST, arg)
        obj.getmark(id)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682165386_IlJmL(x)

def PyCall_1682165386_ChHvn(x):
    for F_G1 in range(0, 1):
        for F_s1 in range(0, 1):
            with open('/dev/null', 'r'):
                for F_Z1 in range(0, 1):
                    W_K1 = 0
                    while (W_K1 in range(0, 1)):
                        W_K1 += 1
                        for F_G1 in range(0, 1):
                            demoFunc(x)

def PyCall_1682165386_IlJmL(x):
    PyCall_1682165386_ChHvn(x)
