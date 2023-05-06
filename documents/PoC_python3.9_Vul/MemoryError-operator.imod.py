 
from operator import *
import operator


def demoFunc(arg1,arg2):
    try:
        ret = operator.imod(arg1, arg2)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
        pass

a= b"b'hhnZJ)uoMtf8CzdP#FBWi!RLUA3jIUIVB0bN%0333333333333r1YuFodxIuzDaR%N'"
b= ""
demoFunc(a,b)
