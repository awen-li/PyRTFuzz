from fuzzwrap import PyDecode 
from sre_parse import *
import sre_parse

API_TYPE_LIST = ['str', 'Pattern']

def demoFunc(arg):
    try:
        (source, state) = PyDecode(API_TYPE_LIST, arg)
        sre_parse.parse_template(source, state)
    except (AssertionError, AttributeError, IndexError, KeyError, LookupError, OSError, OverflowError, TypeError, ValueError, sre_parse.Verbose) as e:
        pass

def RunFuzzer(x):
    PyCall_1681356759_sOPJe(x)

def PyCall_1681356759_sOPJe(x):
    demoFunc(x)
