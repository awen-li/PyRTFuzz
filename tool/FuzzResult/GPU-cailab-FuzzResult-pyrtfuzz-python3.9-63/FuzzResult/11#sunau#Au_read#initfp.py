from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['BytesIO']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = sunau.Au_read(None)
            file = PyDecode(API_TYPE_LIST, arg)
            obj.initfp(file)
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682395882_MdolU(x)

def PyCall_1682395882_wxdGz(x):
    with open('/dev/null', 'r'):
        if True:
            if True:
                if True:
                    dc = demoCls()
                    dc.demoFunc(x)

def PyCall_1682395882_MBAas(x):
    PyCall_1682395882_wxdGz(x)

def PyCall_1682395882_MdolU(x):
    if True:
        PyCall_1682395882_MBAas(x)
