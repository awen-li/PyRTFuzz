from fuzzwrap import PyDecode 
from csv import *
import csv
import re
from io import StringIO

CLS_TYPE_LIST = []
API_TYPE_LIST = ['str', 'str']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = csv.Sniffer()
            (sample, delimiters) = PyDecode(API_TYPE_LIST, arg)
            ret = obj.sniff(sample, delimiters)
            PyPrint(obj)
            repr(obj)
        except (AssertionError, AttributeError, Error, KeyError, LookupError, NameError, OSError, OverflowError, StopIteration, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    for F_z1 in range(0, 1):
        PyCall_1682165158_tmLtl(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682165157_wQcWw(x):
    W_h1 = 0
    while (W_h1 in range(0, 1)):
        W_h1 += 1
        with open('/dev/null', 'r'):
            dc = demoCls()
            dc.demoFunc(x)

def PyCall_1682165158_tmLtl(x):
    with open('/dev/null', 'r'):
        PyCall_1682165157_wQcWw(x)
