from fuzzwrap import PyDecode 
from webbrowser import *
import webbrowser
import copy
import getopt
import shutil
import subprocess
import threading

API_TYPE_LIST = ['str', 'type', 'ExampleBrowser']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (name, klass, instance) = PyDecode(API_TYPE_LIST, arg)
            webbrowser.register(name, klass, instance)
        except (AssertionError, AttributeError, FileNotFoundError, KeyError, LookupError, NotADirectoryError, NotImplementedError, OSError, PermissionError, TypeError, ValueError, copy.Error, getopt.GetoptError, getopt.error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError, subprocess.TimeoutExpired, threading.BrokenBarrierError, webbrowser.Error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
