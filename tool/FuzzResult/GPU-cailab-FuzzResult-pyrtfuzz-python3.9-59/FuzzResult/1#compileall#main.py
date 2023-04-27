from fuzzwrap import PyDecode 
from compileall import *
import compileall
import argparse
import py_compile
import re

API_TYPE_LIST = []

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            ret = compileall.main()
        except (AssertionError, AttributeError, ImportError, KeyboardInterrupt, LookupError, OSError, SyntaxError, TypeError, UnicodeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, py_compile.PyCompileError) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)
