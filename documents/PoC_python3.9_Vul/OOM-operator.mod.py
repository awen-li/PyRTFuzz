from operator import *
import operator


def demoFunc(arg1,arg2):
    try:
        ret = operator.mod(arg1, arg2)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
        pass

a= "11%5999000000rp"
b= ""
demoFunc(a,b)
