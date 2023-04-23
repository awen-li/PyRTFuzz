from fuzzwrap import PyDecode 
from csv import *
import csv
import re
from io import StringIO

CLS_TYPE_LIST = []
API_TYPE_LIST = ['str']

def demoFunc(arg):
    try:
        obj = csv.Sniffer()
        sample = PyDecode(API_TYPE_LIST, arg)
        ret = obj.has_header(sample)
        repr(obj)
    except (AssertionError, AttributeError, Error, KeyError, LookupError, NameError, OSError, OverflowError, StopIteration, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    W_K1 = 0
    while (W_K1 in range(0, 1)):
        W_K1 += 1
        W_x1 = 0
        while (W_x1 in range(0, 1)):
            W_x1 += 1
            demoFunc(x)
