from fuzzwrap import PyDecode 
from distutils.archive_util import *
import distutils
import distutils.archive_util
import os
import tarfile
import zipfile
from distutils.errors import DistutilsExecError
from distutils import log

API_TYPE_LIST = ['str', 'str', 'int', 'int']

def demoFunc(arg):
    try:
        (base_name, base_dir, verbose, dry_run) = PyDecode(API_TYPE_LIST, arg)
        ret = distutils.archive_util.make_zipfile(base_name, base_dir, verbose, dry_run)
    except (AssertionError, AttributeError, DistutilsExecError, ImportError, KeyError, LookupError, OSError, RuntimeError, TypeError, ValueError, tarfile.CompressionError, tarfile.EOFHeaderError, tarfile.EmptyHeaderError, tarfile.ExtractError, tarfile.HeaderError, tarfile.InvalidHeaderError, tarfile.ReadError, tarfile.StreamError, tarfile.SubsequentHeaderError, tarfile.TarError, tarfile.TruncatedHeaderError, zipfile.BadZipFile, zipfile.LargeZipFile) as e:
        pass

def RunFuzzer(x):
    if True:
        demoFunc(x)
