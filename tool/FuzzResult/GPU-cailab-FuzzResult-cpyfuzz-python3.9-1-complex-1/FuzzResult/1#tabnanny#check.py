from fuzzwrap import PyDecode 
from tabnanny import *
import tabnanny
import getopt
import tokenize

API_TYPE_LIST = ['None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            file = PyDecode(API_TYPE_LIST, arg)
            tabnanny.check(file)
        except (AssertionError, AttributeError, IndentationError, LookupError, OSError, TypeError, ValueError, getopt.GetoptError, getopt.error, tabnanny.NannyNag, tokenize.StopTokenizing, tokenize.TokenError) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
