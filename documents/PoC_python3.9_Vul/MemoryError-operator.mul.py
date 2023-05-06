from operator import *
import operator


def demoFunc(arg1,arg2):
    try:
        ret = operator.mul(arg1, arg2)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
        pass

a= 30439031216
b= "!@#$%^&*9523"
demoFunc(a, b)
