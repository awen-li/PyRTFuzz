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
        with open('/dev/null', 'r'):
            for F_e1 in range(0, 1):
                with open('/dev/null', 'r'):
                    W_Y1 = 0
                    while (W_Y1 in range(0, 1)):
                        W_Y1 += 1
                        if True:
                            for F_i1 in range(0, 1):
                                with open('/dev/null', 'r'):
                                    PyCall_1682374940_KGHTk(x)

def PyCall_1682374940_KGHTk(x):
    if True:
        for F_g1 in range(0, 1):
            demoFunc(x)
