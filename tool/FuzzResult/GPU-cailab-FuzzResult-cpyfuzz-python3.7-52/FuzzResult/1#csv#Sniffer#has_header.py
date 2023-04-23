from fuzzwrap import PyDecode 
from csv import *
import csv
import re
from io import StringIO

CLS_TYPE_LIST = []
API_TYPE_LIST = ['str']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = csv.Sniffer()
            sample = PyDecode(API_TYPE_LIST, arg)
            ret = obj.has_header(sample)
        except (AssertionError, AttributeError, Error, KeyError, LookupError, NameError, OSError, OverflowError, StopIteration, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    PyCall_1681356760_jOTQT(x)

def PyCall_1681356760_jOTQT(x):
    dc = demoCls()
    dc.demoFunc(x)
