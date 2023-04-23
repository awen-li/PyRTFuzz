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

def demoFunc(arg):
    try:
        obj = distutils.filelist.FileList()
        (pattern, anchor, prefix, is_regex) = PyDecode(API_TYPE_LIST, arg)
        ret = obj.include_pattern(pattern, anchor, prefix, is_regex)
        repr(obj)
    except (AssertionError, AttributeError, DistutilsInternalError, DistutilsTemplateError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    if True:
        PyCall_1681995693_IkGnR(x)

def PyCall_1681995693_rtCLX(x):
    demoFunc(x)

def PyCall_1681995693_IkGnR(x):
    if True:
        for F_F1 in range(0, 1):
            with open('/dev/null', 'r'):
                W_Y1 = 0
                while (W_Y1 in range(0, 1)):
                    W_Y1 += 1
                    for F_x1 in range(0, 1):
                        with open('/dev/null', 'r'):
                            PyCall_1681995693_rtCLX(x)
