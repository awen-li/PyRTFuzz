from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = sunau.Au_read(None)
        ret = obj.getparams()
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    if True:
        PyCall_1681876665_iFGYQ(x)

def PyCall_1681876665_eKMuf(x):
    if True:
        demoFunc(x)

def PyCall_1681876665_iFGYQ(x):
    with open('/dev/null', 'r'):
        PyCall_1681876665_eKMuf(x)
