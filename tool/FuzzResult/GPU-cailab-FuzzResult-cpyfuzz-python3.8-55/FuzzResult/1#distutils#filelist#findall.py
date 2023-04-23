from fuzzwrap import PyDecode 
from distutils.filelist import *
import distutils
import distutils.filelist
import re
from distutils.errors import DistutilsInternalError
from distutils.errors import DistutilsTemplateError
from distutils import log

API_TYPE_LIST = ['None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            dir = PyDecode(API_TYPE_LIST, arg)
            ret = distutils.filelist.findall(dir)
        except (AssertionError, AttributeError, DistutilsInternalError, DistutilsTemplateError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)
