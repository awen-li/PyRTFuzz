
from operator import *
import operator


def demoFunc(a, b):
    try:
        ret = operator.imod(a, b)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
        pass

demoFunc(b"b'hhnZJ)uoMtf8CzdP#FBWi!RLUA3jIUIVB0bN%0835534333533r1YuFodxIuzDaR%N'", "")
