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

def demoFunc(arg):
    try:
        obj = distutils.filelist.FileList()
        (pattern, anchor, prefix, is_regex) = PyDecode(API_TYPE_LIST, arg)
        ret = obj.exclude_pattern(pattern, anchor, prefix, is_regex)
    except (AssertionError, AttributeError, DistutilsInternalError, DistutilsTemplateError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    PyCall_1681347978_OyUWv(x)

def PyCall_1681347978_OyUWv(x):
    demoFunc(x)
