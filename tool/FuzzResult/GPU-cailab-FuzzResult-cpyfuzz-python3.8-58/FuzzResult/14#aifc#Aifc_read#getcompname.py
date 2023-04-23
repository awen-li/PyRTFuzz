from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = aifc.Aifc_read(None)
        ret = obj.getcompname()
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        for F_q1 in range(0, 1):
            with open('/dev/null', 'r'):
                if True:
                    for F_c1 in range(0, 1):
                        W_K1 = 0
                        while (W_K1 in range(0, 1)):
                            W_K1 += 1
                            for F_x1 in range(0, 1):
                                if True:
                                    with open('/dev/null', 'r'):
                                        for F_k1 in range(0, 1):
                                            PyCall_1682229140_MiSvp(x)

def PyCall_1682229140_MiSvp(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            if True:
                demoFunc(x)
