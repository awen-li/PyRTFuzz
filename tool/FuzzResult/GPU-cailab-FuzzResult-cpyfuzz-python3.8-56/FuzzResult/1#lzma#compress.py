from fuzzwrap import PyDecode 
from lzma import *
import lzma
import io

API_TYPE_LIST = ['bytes', 'int', 'int', 'str', 'int']

def demoFunc(arg):
    try:
        (data, format, check, preset, filters) = PyDecode(API_TYPE_LIST, arg)
        ret = lzma.compress(data, format, check, preset, filters)
    except (AssertionError, AttributeError, LZMAError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        demoFunc(x)
