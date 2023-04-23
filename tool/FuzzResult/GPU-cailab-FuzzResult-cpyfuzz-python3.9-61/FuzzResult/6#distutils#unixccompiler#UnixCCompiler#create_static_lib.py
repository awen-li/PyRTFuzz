from fuzzwrap import PyDecode 
from distutils.unixccompiler import *
import distutils
import distutils.unixccompiler
import re
from distutils.ccompiler import CCompiler
from distutils.errors import DistutilsExecError
from distutils import log
from distutils import sysconfig

CLS_TYPE_LIST = ['NoneType', 'NoneType', 'NoneType']
API_TYPE_LIST = ['list', 'str', 'str', 'NoneType', 'NoneType']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = distutils.unixccompiler.UnixCCompiler()
            (objects, output_libname, output_dir, debug, target_lang) = PyDecode(API_TYPE_LIST, arg)
            obj.create_static_lib(objects, output_libname, output_dir, debug, target_lang)
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, DistutilsExecError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    PyCall_1682200400_JWpcM(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682200400_JWpcM(x):
    W_F1 = 0
    while (W_F1 in range(0, 1)):
        W_F1 += 1
        with open('/dev/null', 'r'):
            dc = demoCls()
            dc.demoFunc(x)
