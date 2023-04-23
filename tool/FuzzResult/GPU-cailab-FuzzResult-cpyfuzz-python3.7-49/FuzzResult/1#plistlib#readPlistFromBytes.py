from fuzzwrap import PyDecode 
from plistlib import *
import plistlib
import re
import struct
from io import BytesIO

API_TYPE_LIST = ['None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            data = PyDecode(API_TYPE_LIST, arg)
            ret = plistlib.readPlistFromBytes(data)
        except (AssertionError, AttributeError, IndexError, LookupError, OSError, OverflowError, TypeError, UnicodeEncodeError, ValueError, plistlib.InvalidFileException, struct.error) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)
