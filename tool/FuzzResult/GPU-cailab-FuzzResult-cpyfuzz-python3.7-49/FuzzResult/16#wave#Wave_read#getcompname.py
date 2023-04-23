from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = wave.Wave_read(None)
        ret = obj.getcompname()
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682251163_MNNBX(x)

def PyCall_1682251163_rgHVR(x):
    demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682251163_qtJRB(x):
    if True:
        if True:
            PyCall_1682251163_rgHVR(x)

def PyCall_1682251163_BjXwE(x):
    W_k1 = 0
    while (W_k1 in range(0, 1)):
        W_k1 += 1
        W_b1 = 0
        while (W_b1 in range(0, 1)):
            W_b1 += 1
            PyCall_1682251163_qtJRB(x)

def PyCall_1682251163_MNNBX(x):
    for F_F1 in range(0, 1):
        with open('/dev/null', 'r'):
            PyCall_1682251163_BjXwE(x)
