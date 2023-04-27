from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = sunau.Au_read(None)
            obj.rewind()
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    for F_s1 in range(0, 1):
        if True:
            PyCall_1682415414_KMUum(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682415414_JKWVU(x):
    for F_O1 in range(0, 1):
        if True:
            for F_L1 in range(0, 1):
                for F_g1 in range(0, 1):
                    W_a1 = 0
                    while (W_a1 in range(0, 1)):
                        W_a1 += 1
                        with open('/dev/null', 'r'):
                            W_R1 = 0
                            while (W_R1 in range(0, 1)):
                                W_R1 += 1
                                W_u1 = 0
                                while (W_u1 in range(0, 1)):
                                    W_u1 += 1
                                    W_H1 = 0
                                    while (W_H1 in range(0, 1)):
                                        W_H1 += 1
                                        dc = demoCls()
                                        dc.demoFunc(x)

def PyCall_1682415414_KMUum(x):
    PyCall_1682415414_JKWVU(x)
