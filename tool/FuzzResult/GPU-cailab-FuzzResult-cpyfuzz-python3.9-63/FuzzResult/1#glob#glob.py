from fuzzwrap import PyDecode 
from glob import *
import glob
import re

API_TYPE_LIST = ['str']

def demoFunc(arg):
    try:
        pathname = PyDecode(API_TYPE_LIST, arg)
        ret = glob.glob(pathname)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)
