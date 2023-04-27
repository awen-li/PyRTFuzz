from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = wave.Wave_read(None)
        ret = obj.getmarkers()
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        if True:
            if True:
                PyCall_1682359382_iOJqt(x)

def PyCall_1682359382_rETaB(x):
    if True:
        if True:
            with open('/dev/null', 'r'):
                demoFunc(x)

def PyCall_1682359382_iOJqt(x):
    with open('/dev/null', 'r'):
        PyCall_1682359382_rETaB(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
