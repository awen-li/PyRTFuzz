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
        except (AssertionError, AttributeError, DistutilsExecError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    PyCall_1682311548_SsSqz(x)

def PyCall_1682311548_jbgvQ(x):
    if True:
        dc = demoCls()
        dc.demoFunc(x)

def PyCall_1682311548_SsSqz(x):
    if True:
        if True:
            PyCall_1682311548_jbgvQ(x)
