from fuzzwrap import PyDecode 
from distutils.util import *
import distutils
import distutils.util
import re
from distutils.errors import DistutilsByteCompileError
from distutils.errors import DistutilsPlatformError
from distutils import log

API_TYPE_LIST = ['None', 'None', 'None', 'None', 'None', 'None']

def demoFunc(arg):
    try:
        (src, dest, template, fixer_names, options, explicit) = PyDecode(API_TYPE_LIST, arg)
        ret = distutils.util.copydir_run_2to3(src, dest, template, fixer_names, options, explicit)
    except (AssertionError, AttributeError, DistutilsByteCompileError, DistutilsPlatformError, ImportError, KeyError, LookupError, OSError, RuntimeError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)
