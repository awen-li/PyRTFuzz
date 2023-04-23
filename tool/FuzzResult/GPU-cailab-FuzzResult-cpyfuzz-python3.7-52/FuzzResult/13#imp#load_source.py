from fuzzwrap import PyDecode 
from imp import *
import imp
import tokenize

API_TYPE_LIST = ['str', 'str', 'TextIOWrapper']

def demoFunc(arg):
    try:
        (name, pathname, file) = PyDecode(API_TYPE_LIST, arg)
        ret = imp.load_source(name, pathname, file)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, RuntimeError, TypeError, ValueError, tokenize.StopTokenizing, tokenize.TokenError) as e:
        pass

def RunFuzzer(x):
    if True:
        PyCall_1682132259_JoSxt(x)

def PyCall_1682132259_wQEvs(x):
    with open('/dev/null', 'r'):
        if True:
            demoFunc(x)

def PyCall_1682132259_JoSxt(x):
    with open('/dev/null', 'r'):
        if True:
            with open('/dev/null', 'r'):
                if True:
                    PyCall_1682132259_wQEvs(x)
