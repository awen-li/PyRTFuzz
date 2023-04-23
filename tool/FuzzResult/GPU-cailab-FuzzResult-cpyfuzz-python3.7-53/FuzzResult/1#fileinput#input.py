from fuzzwrap import PyDecode 
from fileinput import *
import fileinput
import getopt
import gzip

API_TYPE_LIST = ['object', 'object', 'object']

def demoFunc(arg):
    try:
        (files, inplace, backup) = PyDecode(API_TYPE_LIST, arg)
        ret = fileinput.input(files, inplace, backup)
    except (AssertionError, AttributeError, LookupError, OSError, RuntimeError, StopIteration, TypeError, ValueError, getopt.GetoptError, gzip.BadGzipFile) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        demoFunc(x)
