from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        obj = sunau.Au_read(None)
        nframes = PyDecode(API_TYPE_LIST, arg)
        ret = obj.readframes(nframes)
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682337975_KQrls(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682337975_dugbR(x):
    for F_n1 in range(0, 1):
        with open('/dev/null', 'r'):
            demoFunc(x)

def PyCall_1682337975_KQrls(x):
    with open('/dev/null', 'r'):
        if True:
            PyCall_1682337975_dugbR(x)
