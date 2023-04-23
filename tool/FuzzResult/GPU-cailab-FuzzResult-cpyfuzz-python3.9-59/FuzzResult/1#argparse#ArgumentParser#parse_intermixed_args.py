from fuzzwrap import PyDecode 
from argparse import *
import argparse
import copy
import re
import shutil

CLS_TYPE_LIST = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
API_TYPE_LIST = ['None', 'None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = argparse.ArgumentParser()
            (args, namespace) = PyDecode(API_TYPE_LIST, arg)
            ret = obj.parse_intermixed_args(args, namespace)
            repr(obj)
        except (AssertionError, AttributeError, KeyError, LookupError, NotImplementedError, OSError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, copy.Error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)
