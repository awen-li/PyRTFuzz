from fuzzwrap import PyDecode 
from distutils.filelist import *
import distutils
import distutils.filelist
import re
from distutils.errors import DistutilsInternalError
from distutils.errors import DistutilsTemplateError
from distutils import log

CLS_TYPE_LIST = ['NoneType', 'NoneType']
API_TYPE_LIST = ['None', 'None', 'None', 'None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = distutils.filelist.FileList()
            (pattern, anchor, prefix, is_regex) = PyDecode(API_TYPE_LIST, arg)
            ret = obj.exclude_pattern(pattern, anchor, prefix, is_regex)
            PyPrint(obj)
        except (AssertionError, AttributeError, DistutilsInternalError, DistutilsTemplateError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
