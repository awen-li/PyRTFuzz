from fuzzwrap import PyDecode 
from glob import *
import glob
import re

API_TYPE_LIST = ['None', 'None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (dirname, pattern) = PyDecode(API_TYPE_LIST, arg)
            ret = glob.glob1(dirname, pattern)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    PyCall_1681348009_gbexW(x)

def PyCall_1681348009_gbexW(x):
    dc = demoCls()
    dc.demoFunc(x)
