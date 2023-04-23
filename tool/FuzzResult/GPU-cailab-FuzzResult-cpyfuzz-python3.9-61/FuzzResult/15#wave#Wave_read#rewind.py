from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = wave.Wave_read(None)
        obj.rewind()
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682178553_caQxN(x)

def PyCall_1682178553_aNLDQ(x):
    if True:
        with open('/dev/null', 'r'):
            demoFunc(x)

def PyCall_1682178553_dQqWp(x):
    PyCall_1682178553_aNLDQ(x)

def PyCall_1682178553_PyJNw(x):
    PyCall_1682178553_dQqWp(x)

def PyCall_1682178553_cQFRK(x):
    PyCall_1682178553_PyJNw(x)

def PyCall_1682178553_DLGGF(x):
    if True:
        PyCall_1682178553_cQFRK(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682178553_HbiWU(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            if True:
                PyCall_1682178553_DLGGF(x)

def PyCall_1682178553_caQxN(x):
    with open('/dev/null', 'r'):
        PyCall_1682178553_HbiWU(x)
