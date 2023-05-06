from tarfile import *
import tarfile
import argparse
import copy
import io
import re
import shutil
from lzma import LZMAError

def demoFunc(arg1,arg2,arg3):
    try:
        ret = tarfile.itn(arg1,arg2,arg3)
    except (AssertionError, AttributeError, EOFError, FileExistsError, ImportError, KeyError, LZMAError, LookupError, NameError, OSError, TypeError, UnicodeDecodeError, UnicodeEncodeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, copy.Error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError, tarfile.CompressionError, tarfile.EOFHeaderError, tarfile.EmptyHeaderError, tarfile.ExtractError, tarfile.HeaderError, tarfile.InvalidHeaderError, tarfile.ReadError, tarfile.StreamError, tarfile.SubsequentHeaderError, tarfile.TarError, tarfile.TruncatedHeaderError) as e:
        pass

n = 1035465769
digits = 3465813773
format = 2311846708
demoFunc(n, digits, format)
