from fuzzwrap import PyDecode 
from distutils.spawn import *
import distutils
import distutils.spawn
import os
from distutils.errors import DistutilsExecError
from distutils.errors import DistutilsPlatformError
from distutils import log
from distutils import sysconfig

API_TYPE_LIST = ['list', 'int', 'int', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (cmd, search_path, verbose, dry_run) = PyDecode(API_TYPE_LIST, arg)
            distutils.spawn.spawn(cmd, search_path, verbose, dry_run)
        except (AssertionError, AttributeError, DistutilsExecError, DistutilsPlatformError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    if True:
        if True:
            PyCall_1682126081_gCkBy(x)

def PyCall_1682126081_gCkBy(x):
    dc = demoCls()
    dc.demoFunc(x)
