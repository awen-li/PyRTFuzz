from fuzzwrap import PyDecode 
from plistlib import *
import plistlib
import re
import struct
from io import BytesIO

API_TYPE_LIST = ['bytes']

def demoFunc(arg):
    try:
        value = PyDecode(API_TYPE_LIST, arg)
        ret = plistlib.loads(value)
    except (AssertionError, AttributeError, IndexError, LookupError, OSError, OverflowError, TypeError, UnicodeEncodeError, ValueError, plistlib.InvalidFileException, struct.error) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)
