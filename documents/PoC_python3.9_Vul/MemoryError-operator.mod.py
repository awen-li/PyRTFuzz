from operator import *
import operator


def demoFunc(arg1,arg2):
    try:
        ret = operator.mod(arg1, arg2)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
        pass

a= "155%7000000000000ret00000015082063?0000000000000000p1155900000005082063303862299307%+4"
b= "!@#$%^&*9523"
demoFunc(a,b)
