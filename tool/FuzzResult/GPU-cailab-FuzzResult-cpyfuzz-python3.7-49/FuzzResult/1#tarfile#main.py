from fuzzwrap import PyDecode 
from tarfile import *
import tarfile
import argparse
import copy
import io
import re
import shutil
from lzma import LZMAError

API_TYPE_LIST = []

def demoFunc(arg):
    try:
        tarfile.main()
    except (AssertionError, AttributeError, EOFError, FileExistsError, ImportError, KeyError, LZMAError, LookupError, NameError, OSError, TypeError, UnicodeDecodeError, UnicodeEncodeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, copy.Error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError, tarfile.CompressionError, tarfile.EOFHeaderError, tarfile.EmptyHeaderError, tarfile.ExtractError, tarfile.HeaderError, tarfile.InvalidHeaderError, tarfile.ReadError, tarfile.StreamError, tarfile.SubsequentHeaderError, tarfile.TarError, tarfile.TruncatedHeaderError) as e:
        pass

def RunFuzzer(x):
    PyCall_1681356766_iAFAR(x)

def PyCall_1681356766_iAFAR(x):
    demoFunc(x)
