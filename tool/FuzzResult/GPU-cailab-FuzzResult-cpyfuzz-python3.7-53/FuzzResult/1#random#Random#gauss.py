from fuzzwrap import PyDecode 
from random import *
import random
from math import e

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = random.Random()
            (mu, sigma) = PyDecode(API_TYPE_LIST, arg)
            ret = obj.gauss(mu, sigma)
        except (AssertionError, AttributeError, ImportError, LookupError, NotImplementedError, OSError, TypeError, ValueError, ZeroDivisionError) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
