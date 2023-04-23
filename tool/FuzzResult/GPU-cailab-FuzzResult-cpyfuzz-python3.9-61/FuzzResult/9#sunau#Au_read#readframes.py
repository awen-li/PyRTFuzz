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
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682199968_ccxCH(x)

def PyCall_1682199968_ccxCH(x):
    with open('/dev/null', 'r'):
        if True:
            with open('/dev/null', 'r'):
                with open('/dev/null', 'r'):
                    if True:
                        with open('/dev/null', 'r'):
                            if True:
                                demoFunc(x)
