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
        PyPrint(obj)
    except (AssertionError, AttributeError, Error, KeyError, LookupError, NameError, OSError, OverflowError, StopIteration, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    if True:
        demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
