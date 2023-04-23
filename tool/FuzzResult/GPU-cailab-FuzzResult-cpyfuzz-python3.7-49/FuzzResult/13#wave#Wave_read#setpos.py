from fuzzwrap import PyDecode 
from wave import *
import wave
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        obj = wave.Wave_read(None)
        pos = PyDecode(API_TYPE_LIST, arg)
        obj.setpos(pos)
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, struct.error, wave.Error) as e:
        pass

def RunFuzzer(x):
    if True:
        with open('/dev/null', 'r'):
            if True:
                with open('/dev/null', 'r'):
                    PyCall_1682177483_OChDp(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682177483_sqLyP(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            if True:
                demoFunc(x)

def PyCall_1682177483_OChDp(x):
    PyCall_1682177483_sqLyP(x)
