from fuzzwrap import PyDecode 
from pprint import *
import pprint
import re
from io import StringIO

API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        object = PyDecode(API_TYPE_LIST, arg)
        ret = pprint.isrecursive(object)
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, LookupError, OSError, StopIteration, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        if True:
            if True:
                PyCall_1682140859_ZTCGg(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682140859_ZTCGg(x):
    demoFunc(x)
