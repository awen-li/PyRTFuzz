from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        obj = aifc.Aifc_read(None)
        nframes = PyDecode(API_TYPE_LIST, arg)
        ret = obj.readframes(nframes)
        repr(obj)
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                PyCall_1682172937_utFQi(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682172937_utFQi(x):
    with open('/dev/null', 'r'):
        if True:
            with open('/dev/null', 'r'):
                demoFunc(x)
