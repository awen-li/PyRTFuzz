from fuzzwrap import PyDecode 
from plistlib import *
import plistlib
import re
import struct
from io import BytesIO

API_TYPE_LIST = ['BytesIO']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            fp = PyDecode(API_TYPE_LIST, arg)
            ret = plistlib.load(fp)
        except (AssertionError, AttributeError, IndexError, LookupError, OSError, OverflowError, TypeError, UnicodeEncodeError, ValueError, plistlib.InvalidFileException, struct.error) as e:
            pass

def RunFuzzer(x):
    PyCall_1681352793_BjLfQ(x)

def PyCall_1681352793_BjLfQ(x):
    dc = demoCls()
    dc.demoFunc(x)
