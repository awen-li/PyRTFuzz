from fuzzwrap import PyDecode 
from distutils.filelist import *
import distutils
import distutils.filelist
import re
from distutils.errors import DistutilsInternalError
from distutils.errors import DistutilsTemplateError
from distutils import log

CLS_TYPE_LIST = ['NoneType', 'NoneType']
API_TYPE_LIST = ['str', 'int', 'str', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = distutils.filelist.FileList()
            (pattern, anchor, prefix, is_regex) = PyDecode(API_TYPE_LIST, arg)
            ret = obj.include_pattern(pattern, anchor, prefix, is_regex)
        except (AssertionError, AttributeError, DistutilsInternalError, DistutilsTemplateError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
