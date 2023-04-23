from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = aifc.Aifc_read(None)
        ret = obj.getnchannels()
        repr(obj)
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        if True:
            PyCall_1682165064_rxrVr(x)

def PyCall_1682165064_ojsOQ(x):
    if True:
        with open('/dev/null', 'r'):
            demoFunc(x)

def PyCall_1682165064_rxrVr(x):
    if True:
        PyCall_1682165064_ojsOQ(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
