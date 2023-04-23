from fuzzwrap import PyDecode 
from base64 import *
import base64
import binascii
import getopt
import struct

API_TYPE_LIST = []

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            base64.main()
        except (AssertionError, AttributeError, KeyError, LookupError, OSError, TypeError, UnicodeEncodeError, ValueError, binascii.Error, getopt.GetoptError, getopt.error, struct.error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
