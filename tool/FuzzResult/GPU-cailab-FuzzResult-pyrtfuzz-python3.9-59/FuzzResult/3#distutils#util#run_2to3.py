from fuzzwrap import PyDecode 
from distutils.util import *
import distutils
import distutils.util
from distutils.errors import DistutilsByteCompileError
from distutils.errors import DistutilsPlatformError
from distutils import log

API_TYPE_LIST = ['None', 'None', 'None', 'None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (files, fixer_names, options, explicit) = PyDecode(API_TYPE_LIST, arg)
            distutils.util.run_2to3(files, fixer_names, options, explicit)
        except (AssertionError, AttributeError, DistutilsByteCompileError, DistutilsPlatformError, ImportError, KeyError, LookupError, OSError, RuntimeError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    PyCall_1682349880_bfqmr(x)

def PyCall_1682349880_bfqmr(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
