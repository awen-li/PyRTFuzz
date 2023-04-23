from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = wave.Wave_read(None)
        ret = obj.getparams()
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682104817_haStL(x)

def PyCall_1682104817_ZcNVd(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            demoFunc(x)

def PyCall_1682104817_haStL(x):
    with open('/dev/null', 'r'):
        PyCall_1682104817_ZcNVd(x)
