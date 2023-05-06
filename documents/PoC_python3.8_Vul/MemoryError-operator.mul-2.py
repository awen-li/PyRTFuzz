
from operator import *
import operator

def demoFunc(a, b):
    try:
        ret = operator.mul(a, b)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
        pass

a = 4211630933
b = "305qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq0242788"
demoFunc(a, b)
