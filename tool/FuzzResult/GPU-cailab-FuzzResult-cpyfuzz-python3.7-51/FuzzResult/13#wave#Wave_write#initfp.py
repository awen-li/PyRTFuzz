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
        repr(obj)
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        if True:
            if True:
                if True:
                    if True:
                        with open('/dev/null', 'r'):
                            PyCall_1682217554_ACNax(x)

def PyCall_1682217554_ACNax(x):
    demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
