from fuzzwrap import PyDecode 
from compileall import *
import compileall
import argparse
import py_compile
import re

API_TYPE_LIST = ['str', 'int', 'str', 'bool', 'NoneType', 'bool', 'bool', 'int', 'int', 'NoneType']

def demoFunc(arg):
    try:
        (dir, maxlevels, ddir, force, rx, quiet, legacy, optimize, workers, invalidation_mode) = PyDecode(API_TYPE_LIST, arg)
        ret = compileall.compile_dir(dir, maxlevels, ddir, force, rx, quiet, legacy, optimize, workers, invalidation_mode)
    except (AssertionError, AttributeError, ImportError, KeyboardInterrupt, LookupError, OSError, SyntaxError, TypeError, UnicodeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, py_compile.PyCompileError) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        for F_V1 in range(0, 1):
            PyCall_1682132042_FlpiH(x)

def PyCall_1682132042_FlpiH(x):
    W_j1 = 0
    while (W_j1 in range(0, 1)):
        W_j1 += 1
        for F_z1 in range(0, 1):
            for F_i1 in range(0, 1):
                for F_p1 in range(0, 1):
                    with open('/dev/null', 'r'):
                        with open('/dev/null', 'r'):
                            W_a1 = 0
                            while (W_a1 in range(0, 1)):
                                W_a1 += 1
                                with open('/dev/null', 'r'):
                                    W_Z1 = 0
                                    while (W_Z1 in range(0, 1)):
                                        W_Z1 += 1
                                        demoFunc(x)
