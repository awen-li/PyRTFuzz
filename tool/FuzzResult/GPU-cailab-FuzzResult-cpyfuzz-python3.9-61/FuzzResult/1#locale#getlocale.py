from fuzzwrap import PyDecode 
from locale import *
import locale
import re

API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        category = PyDecode(API_TYPE_LIST, arg)
        ret = locale.getlocale(category)
    except (AssertionError, AttributeError, Error, ImportError, LookupError, NameError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        demoFunc(x)
