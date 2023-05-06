
from locale import *
import locale
import re
from builtins import str

def demoFunc(f):
    try:
        ret = locale.format_string(f, 2)
    except (AssertionError, AttributeError, Error, ImportError, LookupError, NameError, OSError, TypeError, ValueError) as e:
        pass

demoFunc("%9985325346ss")
