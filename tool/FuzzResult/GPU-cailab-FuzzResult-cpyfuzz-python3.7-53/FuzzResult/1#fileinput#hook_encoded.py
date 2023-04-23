from fuzzwrap import PyDecode 
from fileinput import *
import fileinput
import getopt
import gzip

API_TYPE_LIST = ['str', 'object']

def demoFunc(arg):
    try:
        (encoding, errors) = PyDecode(API_TYPE_LIST, arg)
        ret = fileinput.hook_encoded(encoding, errors)
    except (AssertionError, AttributeError, LookupError, OSError, RuntimeError, StopIteration, TypeError, ValueError, getopt.GetoptError, gzip.BadGzipFile) as e:
        pass

def RunFuzzer(x):
    PyCall_1681356754_ELHYp(x)

def PyCall_1681356754_ELHYp(x):
    demoFunc(x)
