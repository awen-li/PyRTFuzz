from fuzzwrap import PyDecode 
from gzip import *
import gzip
import io

API_TYPE_LIST = ['BytesIO', 'int']

def demoFunc(arg):
    try:
        (output, value) = PyDecode(API_TYPE_LIST, arg)
        gzip.write32u(output, value)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, UnicodeEncodeError, ValueError, gzip.BadGzipFile) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)
