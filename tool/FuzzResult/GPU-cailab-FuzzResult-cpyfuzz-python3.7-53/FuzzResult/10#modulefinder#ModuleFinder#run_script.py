from fuzzwrap import PyDecode 
from modulefinder import *
import modulefinder

CLS_TYPE_LIST = ['NoneType', 'NoneType', 'NoneType', 'NoneType']
API_TYPE_LIST = ['None']

def demoFunc(arg):
    try:
        obj = modulefinder.ModuleFinder()
        pathname = PyDecode(API_TYPE_LIST, arg)
        obj.run_script(pathname)
        PyPrint(obj)
    except (AssertionError, AttributeError, ImportError, KeyError, KeyboardInterrupt, LookupError, OSError, RuntimeError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    if True:
        if True:
            for F_Y1 in range(0, 1):
                for F_e1 in range(0, 1):
                    with open('/dev/null', 'r'):
                        if True:
                            for F_P1 in range(0, 1):
                                demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
