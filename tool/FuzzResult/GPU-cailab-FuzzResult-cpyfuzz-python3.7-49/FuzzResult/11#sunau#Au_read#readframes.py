from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = sunau.Au_read(None)
            nframes = PyDecode(API_TYPE_LIST, arg)
            ret = obj.readframes(nframes)
            PyPrint(obj)
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    if True:
        PyCall_1682125777_wkiDh(x)

def PyCall_1682125777_miIio(x):
    dc = demoCls()
    dc.demoFunc(x)

def PyCall_1682125777_dbjOx(x):
    PyCall_1682125777_miIio(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682125777_FKMtp(x):
    with open('/dev/null', 'r'):
        PyCall_1682125777_dbjOx(x)

def PyCall_1682125777_wkiDh(x):
    with open('/dev/null', 'r'):
        PyCall_1682125777_FKMtp(x)
