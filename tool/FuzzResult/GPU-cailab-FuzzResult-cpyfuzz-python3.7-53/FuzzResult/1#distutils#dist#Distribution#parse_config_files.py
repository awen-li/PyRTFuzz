from fuzzwrap import PyDecode 
from distutils.dist import *
import distutils
import distutils.dist
from distutils import log

CLS_TYPE_LIST = []
API_TYPE_LIST = ['None']

def demoFunc(arg):
    try:
        obj = distutils.dist.Distribution()
        filenames = PyDecode(API_TYPE_LIST, arg)
        obj.parse_config_files(filenames)
    except (AssertionError, AttributeError, DistutilsArgError, DistutilsClassError, DistutilsModuleError, DistutilsOptionError, ImportError, LookupError, OSError, SystemExit, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        demoFunc(x)
