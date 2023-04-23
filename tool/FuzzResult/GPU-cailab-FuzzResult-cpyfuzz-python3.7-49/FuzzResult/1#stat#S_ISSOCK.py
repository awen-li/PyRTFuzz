from fuzzwrap import PyDecode 
from stat import *
import stat

API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        mode = PyDecode(API_TYPE_LIST, arg)
        ret = stat.S_ISSOCK(mode)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        demoFunc(x)
