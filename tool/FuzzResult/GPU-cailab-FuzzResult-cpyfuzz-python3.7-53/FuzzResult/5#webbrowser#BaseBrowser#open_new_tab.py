from fuzzwrap import PyDecode 
from webbrowser import *
import webbrowser
import copy
import getopt
import shutil
import subprocess
import threading

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['None']

def demoFunc(arg):
    try:
        obj = webbrowser.BaseBrowser()
        url = PyDecode(API_TYPE_LIST, arg)
        ret = obj.open_new_tab(url)
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, FileNotFoundError, KeyError, LookupError, NotImplementedError, OSError, TypeError, ValueError, copy.Error, getopt.GetoptError, getopt.error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError, subprocess.TimeoutExpired, threading.BrokenBarrierError, webbrowser.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
