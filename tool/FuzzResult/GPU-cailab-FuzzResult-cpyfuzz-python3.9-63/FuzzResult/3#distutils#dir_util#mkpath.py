from fuzzwrap import PyDecode 
from distutils.dir_util import *
import distutils
import distutils.dir_util
import os
from distutils.errors import DistutilsFileError
from distutils.errors import DistutilsInternalError
from distutils import log

API_TYPE_LIST = ['str', 'int', 'int', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (name, mode, verbose, dry_run) = PyDecode(API_TYPE_LIST, arg)
            ret = distutils.dir_util.mkpath(name, mode, verbose, dry_run)
        except (AssertionError, AttributeError, DistutilsFileError, DistutilsInternalError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        if True:
            if True:
                dc = demoCls()
                dc.demoFunc(x)
