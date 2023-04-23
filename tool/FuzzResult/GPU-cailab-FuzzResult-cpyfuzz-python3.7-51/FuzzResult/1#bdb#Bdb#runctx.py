from fuzzwrap import PyDecode 
from bdb import *
import bdb

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['None', 'None', 'None']

def demoFunc(arg):
    try:
        obj = bdb.Bdb()
        (cmd, globals, locals) = PyDecode(API_TYPE_LIST, arg)
        obj.runctx(cmd, globals, locals)
        PyPrint(obj)
    except (AssertionError, AttributeError, IndexError, LookupError, NotImplementedError, OSError, TypeError, ValueError, bdb.BdbQuit) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
