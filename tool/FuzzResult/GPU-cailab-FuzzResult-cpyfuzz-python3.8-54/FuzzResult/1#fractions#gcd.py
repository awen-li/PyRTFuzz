from fuzzwrap import PyDecode 
from fractions import *
import fractions
import re

API_TYPE_LIST = ['int', 'int']

def demoFunc(arg):
    try:
        (a, b) = PyDecode(API_TYPE_LIST, arg)
        ret = fractions.gcd(a, b)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, ZeroDivisionError) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)
