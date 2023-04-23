from fuzzwrap import PyDecode 
from zipfile import *
import zipfile
import argparse
import io
import shutil
import threading
import time

API_TYPE_LIST = ['None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            args = PyDecode(API_TYPE_LIST, arg)
            zipfile.main(args)
        except (AssertionError, AttributeError, DeprecationWarning, EOFError, ImportError, KeyError, LookupError, NotImplementedError, OSError, RuntimeError, TypeError, UnicodeEncodeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, io.UnsupportedOperation, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError, threading.BrokenBarrierError, zipfile.BadZipFile, zipfile.LargeZipFile) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
