from fuzzwrap import PyDecode 
from gettext import *
import gettext
import copy
import re

API_TYPE_LIST = ['str']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            plural = PyDecode(API_TYPE_LIST, arg)
            ret = gettext.c2py(plural)
        except (AssertionError, AttributeError, FileNotFoundError, KeyError, LookupError, OSError, RecursionError, TypeError, ValueError, copy.Error) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)
