from fuzzwrap import PyDecode 
from plistlib import *
import plistlib
import re
import struct
from io import BytesIO

API_TYPE_LIST = ['bytes']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            value = PyDecode(API_TYPE_LIST, arg)
            ret = plistlib.loads(value)
        except (AssertionError, AttributeError, IndexError, LookupError, OSError, OverflowError, TypeError, UnicodeEncodeError, ValueError, plistlib.InvalidFileException, struct.error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
