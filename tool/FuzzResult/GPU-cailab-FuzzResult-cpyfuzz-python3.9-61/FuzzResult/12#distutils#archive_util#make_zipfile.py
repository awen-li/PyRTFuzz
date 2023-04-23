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
    PyCall_1682225111_gATns(x)

def PyCall_1682225111_exwwK(x):
    for F_d1 in range(0, 1):
        for F_P1 in range(0, 1):
            W_L1 = 0
            while (W_L1 in range(0, 1)):
                W_L1 += 1
                for F_g1 in range(0, 1):
                    if True:
                        demoFunc(x)

def PyCall_1682225111_KxRrQ(x):
    W_w1 = 0
    while (W_w1 in range(0, 1)):
        W_w1 += 1
        PyCall_1682225111_exwwK(x)

def PyCall_1682225111_gATns(x):
    PyCall_1682225111_KxRrQ(x)
