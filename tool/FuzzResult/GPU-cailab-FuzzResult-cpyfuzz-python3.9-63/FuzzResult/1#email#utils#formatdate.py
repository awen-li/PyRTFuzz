from fuzzwrap import PyDecode 
from email.utils import *
import email
import email.utils
import re
import time

API_TYPE_LIST = ['float', 'bool', 'bool']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (timeval, localtime, usegmt) = PyDecode(API_TYPE_LIST, arg)
            ret = email.utils.formatdate(timeval, localtime, usegmt)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, UnicodeEncodeError, ValueError) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
