from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = sunau.Au_write(None)
        ret = obj.getsampwidth()
        repr(obj)
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            PyCall_1682222793_sXImW(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682222793_sXImW(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            for F_n1 in range(0, 1):
                for F_s1 in range(0, 1):
                    for F_J1 in range(0, 1):
                        demoFunc(x)
