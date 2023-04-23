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
    demoFunc(x)
