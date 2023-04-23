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
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        for F_z1 in range(0, 1):
            W_e1 = 0
            while (W_e1 in range(0, 1)):
                W_e1 += 1
                if True:
                    for F_u1 in range(0, 1):
                        PyCall_1682149986_FwKrO(x)

def PyCall_1682149986_QSFVl(x):
    if True:
        W_n1 = 0
        while (W_n1 in range(0, 1)):
            W_n1 += 1
            dc = demoCls()
            dc.demoFunc(x)

def PyCall_1682149986_sjiur(x):
    PyCall_1682149986_QSFVl(x)

def PyCall_1682149986_TZyuk(x):
    W_M1 = 0
    while (W_M1 in range(0, 1)):
        W_M1 += 1
        PyCall_1682149986_sjiur(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682149986_FwKrO(x):
    W_C1 = 0
    while (W_C1 in range(0, 1)):
        W_C1 += 1
        W_K1 = 0
        while (W_K1 in range(0, 1)):
            W_K1 += 1
            PyCall_1682149986_TZyuk(x)
