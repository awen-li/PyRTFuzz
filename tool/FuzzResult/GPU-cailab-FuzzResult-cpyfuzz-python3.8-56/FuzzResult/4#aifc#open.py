from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

API_TYPE_LIST = ['BytesIO', 'str']

def demoFunc(arg):
    try:
        (f, mode) = PyDecode(API_TYPE_LIST, arg)
        ret = aifc.open(f, mode)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        W_P1 = 0
        while (W_P1 in range(0, 1)):
            W_P1 += 1
            PyCall_1682265511_wmFzJ(x)

def PyCall_1682265511_wmFzJ(x):
    if True:
        demoFunc(x)
