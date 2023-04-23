from fuzzwrap import PyDecode 
from sunau import *
import sunau

API_TYPE_LIST = ['str', 'str']

def demoFunc(arg):
    try:
        (f, mode) = PyDecode(API_TYPE_LIST, arg)
        ret = sunau.openfp(f, mode)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        PyCall_1682105614_euOVB(x)

def PyCall_1682105614_euOVB(x):
    if True:
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                demoFunc(x)
