from fuzzwrap import PyDecode 
from glob import *
import glob
import re

API_TYPE_LIST = ['None', 'None']

def demoFunc(arg):
    try:
        (dirname, pattern) = PyDecode(API_TYPE_LIST, arg)
        ret = glob.glob1(dirname, pattern)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    PyCall_1681352800_sPUAK(x)

def PyCall_1681352800_sPUAK(x):
    demoFunc(x)
