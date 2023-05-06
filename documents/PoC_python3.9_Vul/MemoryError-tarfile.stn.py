from tarfile import *
import tarfile
import argparse
import copy
import io
import re
import shutil
from builtins import open
from lzma import LZMAError


def demoFunc(arg1,arg2,arg3,arg4):
    try:
        ret = tarfile.stn(arg1,arg2,arg3,arg4)
    except (AssertionError, AttributeError, EOFError, Exception, FileExistsError, ImportError, KeyError, LZMAError, LookupError, NameError, OSError, TypeError, UnicodeDecodeError, UnicodeEncodeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, copy.Error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError, tarfile.CompressionError, tarfile.EOFHeaderError, tarfile.EmptyHeaderError, tarfile.ExtractError, tarfile.HeaderError, tarfile.InvalidHeaderError, tarfile.ReadError, tarfile.StreamError, tarfile.SubsequentHeaderError, tarfile.TarError, tarfile.TruncatedHeaderError) as e:
        pass

s= "z0D3%MS"
length= 6148914691236517206
encoding= "775"
errors= "r(KA0z%zU"
demoFunc(s, length, encoding, errors)
