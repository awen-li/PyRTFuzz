 
from operator import *
import operator


def demoFunc(arg1,arg2):
    try:
        ret = operator.imod(arg1, arg2)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
        pass

a= b"%9993333333r"
b= ""
demoFunc(a,b)
