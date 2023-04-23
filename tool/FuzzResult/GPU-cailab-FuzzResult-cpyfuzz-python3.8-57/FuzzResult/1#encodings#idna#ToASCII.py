from fuzzwrap import PyDecode 
from encodings.idna import *
import encodings
import encodings.idna
import re

API_TYPE_LIST = ['str']

def demoFunc(arg):
    try:
        label = PyDecode(API_TYPE_LIST, arg)
        ret = encodings.idna.ToASCII(label)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, UnicodeDecodeError, UnicodeEncodeError, UnicodeError, ValueError) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)
