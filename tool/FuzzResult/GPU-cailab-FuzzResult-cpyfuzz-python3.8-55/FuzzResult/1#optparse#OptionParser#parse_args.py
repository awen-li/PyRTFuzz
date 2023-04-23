from fuzzwrap import PyDecode 
from optparse import *
import optparse

CLS_TYPE_LIST = ['NoneType', 'NoneType', 'NoneType', 'NoneType', 'NoneType', 'NoneType', 'NoneType', 'NoneType', 'NoneType', 'NoneType']
API_TYPE_LIST = ['NoneType', 'NoneType']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = optparse.OptionParser()
            (args, values) = PyDecode(API_TYPE_LIST, arg)
            ret = obj.parse_args(args, values)
        except (AssertionError, AttributeError, ImportError, LookupError, NotImplementedError, OSError, TypeError, ValueError, optparse.AmbiguousOptionError, optparse.BadOptionError, optparse.OptParseError, optparse.OptionConflictError, optparse.OptionError, optparse.OptionValueError) as e:
            pass

def RunFuzzer(x):
    PyCall_1681352798_BICdR(x)

def PyCall_1681352798_BICdR(x):
    dc = demoCls()
    dc.demoFunc(x)
