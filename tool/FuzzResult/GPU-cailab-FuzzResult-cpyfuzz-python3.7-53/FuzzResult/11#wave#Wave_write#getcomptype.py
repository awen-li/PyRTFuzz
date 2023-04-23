from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = wave.Wave_write(None)
        ret = obj.getcomptype()
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    if True:
        with open('/dev/null', 'r'):
            PyCall_1682158671_QpnuR(x)

def PyCall_1682158671_QpnuR(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            if True:
                if True:
                    demoFunc(x)
