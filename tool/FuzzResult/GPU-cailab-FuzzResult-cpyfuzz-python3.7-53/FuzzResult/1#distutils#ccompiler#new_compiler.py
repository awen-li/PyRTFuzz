from fuzzwrap import PyDecode 
from distutils.ccompiler import *
import distutils
import distutils.ccompiler
import os
import re
from distutils import log

API_TYPE_LIST = ['NoneType', 'NoneType', 'int', 'int', 'int']

def demoFunc(arg):
    try:
        (plat, compiler, verbose, dry_run, force) = PyDecode(API_TYPE_LIST, arg)
        ret = distutils.ccompiler.new_compiler(plat, compiler, verbose, dry_run, force)
    except (AssertionError, AttributeError, CompileError, ImportError, KeyError, LinkError, LookupError, NotImplementedError, OSError, TypeError, UnknownFileError, ValueError) as e:
        pass

def RunFuzzer(x):
    PyCall_1681356743_YBbNf(x)

def PyCall_1681356743_YBbNf(x):
    demoFunc(x)
