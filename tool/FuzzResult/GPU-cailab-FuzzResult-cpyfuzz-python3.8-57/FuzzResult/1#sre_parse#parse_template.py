from fuzzwrap import PyDecode 
from sre_parse import *
import sre_parse

API_TYPE_LIST = ['str', 'Pattern']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (source, state) = PyDecode(API_TYPE_LIST, arg)
            sre_parse.parse_template(source, state)
        except (AssertionError, AttributeError, IndexError, KeyError, LookupError, OSError, OverflowError, TypeError, ValueError, sre_parse.Verbose) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
