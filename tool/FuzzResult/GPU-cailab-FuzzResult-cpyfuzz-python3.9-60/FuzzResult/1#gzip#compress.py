from fuzzwrap import PyDecode 
from gzip import *
import gzip
import io

API_TYPE_LIST = ['bytes', 'int']

def demoFunc(arg):
    try:
        (data, compresslevel) = PyDecode(API_TYPE_LIST, arg)
        ret = gzip.compress(data, compresslevel)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, UnicodeEncodeError, ValueError, gzip.BadGzipFile) as e:
        pass

def RunFuzzer(x):
    PyCall_1681347991_bIVAG(x)

def PyCall_1681347991_bIVAG(x):
    demoFunc(x)
