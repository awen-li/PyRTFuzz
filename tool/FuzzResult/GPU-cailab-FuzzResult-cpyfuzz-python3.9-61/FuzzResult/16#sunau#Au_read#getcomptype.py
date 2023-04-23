from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = sunau.Au_read(None)
        ret = obj.getcomptype()
        repr(obj)
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    for F_A1 in range(0, 1):
        W_z1 = 0
        while (W_z1 in range(0, 1)):
            W_z1 += 1
            W_D1 = 0
            while (W_D1 in range(0, 1)):
                W_D1 += 1
                with open('/dev/null', 'r'):
                    if True:
                        with open('/dev/null', 'r'):
                            for F_j1 in range(0, 1):
                                W_L1 = 0
                                while (W_L1 in range(0, 1)):
                                    W_L1 += 1
                                    for F_Z1 in range(0, 1):
                                        for F_F1 in range(0, 1):
                                            if True:
                                                demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
