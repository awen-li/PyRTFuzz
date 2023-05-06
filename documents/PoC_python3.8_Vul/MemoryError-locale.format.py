
from locale import *
import locale
import re
from builtins import str

def demoFunc(percent, value):
    try:
        ret = locale.format(percent, value)
    except (AssertionError, AttributeError, Error, ImportError, LookupError, NameError, OSError, TypeError, ValueError) as e:
        pass

demoFunc("%9999991111111s", 2)
