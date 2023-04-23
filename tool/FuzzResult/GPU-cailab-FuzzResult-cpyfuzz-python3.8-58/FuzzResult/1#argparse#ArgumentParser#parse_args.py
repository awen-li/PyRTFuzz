from fuzzwrap import PyDecode 
from argparse import *
import argparse
import copy
import re
import shutil

CLS_TYPE_LIST = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
API_TYPE_LIST = ['list', 'TestProgram']

def demoFunc(arg):
    try:
        obj = argparse.ArgumentParser()
        (args, namespace) = PyDecode(API_TYPE_LIST, arg)
        ret = obj.parse_args(args, namespace)
    except (AssertionError, AttributeError, KeyError, LookupError, NotImplementedError, OSError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, copy.Error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError) as e:
        pass

def RunFuzzer(x):
    if True:
        demoFunc(x)
