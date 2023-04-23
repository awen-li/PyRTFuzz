from fuzzwrap import PyDecode 
from bz2 import *
import bz2
import io

API_TYPE_LIST = ['bytearray', 'int']

def demoFunc(arg):
    try:
        (data, compresslevel) = PyDecode(API_TYPE_LIST, arg)
        ret = bz2.compress(data, compresslevel)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)
