from fuzzwrap import PyDecode 
from getpass import *
import getpass
import io
import os
import termios

API_TYPE_LIST = ['str', 'Mock']

def demoFunc(arg):
    try:
        (prompt, stream) = PyDecode(API_TYPE_LIST, arg)
        ret = getpass.unix_getpass(prompt, stream)
    except (AssertionError, AttributeError, EOFError, ImportError, KeyboardInterrupt, LookupError, OSError, TypeError, UnicodeEncodeError, ValueError, getpass.GetPassWarning, termios.error) as e:
        pass

def RunFuzzer(x):
    PyCall_1681347995_yOmSg(x)

def PyCall_1681347995_yOmSg(x):
    demoFunc(x)
