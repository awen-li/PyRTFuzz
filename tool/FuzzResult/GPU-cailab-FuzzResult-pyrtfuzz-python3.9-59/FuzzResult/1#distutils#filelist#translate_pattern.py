from fuzzwrap import PyDecode 
from distutils.filelist import *
import distutils
import distutils.filelist
import re
from distutils.errors import DistutilsInternalError
from distutils.errors import DistutilsTemplateError
from distutils import log

API_TYPE_LIST = ['None', 'None', 'None', 'None']

def demoFunc(arg):
    try:
        (pattern, anchor, prefix, is_regex) = PyDecode(API_TYPE_LIST, arg)
        ret = distutils.filelist.translate_pattern(pattern, anchor, prefix, is_regex)
    except (AssertionError, AttributeError, DistutilsInternalError, DistutilsTemplateError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)
