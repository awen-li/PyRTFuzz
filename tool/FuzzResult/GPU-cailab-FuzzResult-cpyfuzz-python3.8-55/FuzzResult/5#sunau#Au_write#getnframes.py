from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = sunau.Au_write(None)
        ret = obj.getnframes()
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            if True:
                PyCall_1682188520_kYKWu(x)

def PyCall_1682188520_hxfhs(x):
    demoFunc(x)

def PyCall_1682188520_kYKWu(x):
    PyCall_1682188520_hxfhs(x)
