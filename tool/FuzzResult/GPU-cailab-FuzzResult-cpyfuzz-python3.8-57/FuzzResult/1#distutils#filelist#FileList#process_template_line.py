from fuzzwrap import PyDecode 
from distutils.filelist import *
import distutils
import distutils.filelist
import re
from distutils.errors import DistutilsInternalError
from distutils.errors import DistutilsTemplateError
from distutils import log

CLS_TYPE_LIST = ['NoneType', 'NoneType']
API_TYPE_LIST = ['None']

def demoFunc(arg):
    try:
        obj = distutils.filelist.FileList()
        line = PyDecode(API_TYPE_LIST, arg)
        obj.process_template_line(line)
        repr(obj)
    except (AssertionError, AttributeError, DistutilsInternalError, DistutilsTemplateError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)
