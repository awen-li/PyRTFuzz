from fuzzwrap import PyDecode 
from webbrowser import *
import webbrowser
import copy
import getopt
import os
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
        if True:
            if True:
                PyCall_1682152177_uBDuR(x)

def PyCall_1682152177_LnosU(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            dc = demoCls()
            dc.demoFunc(x)

def PyCall_1682152177_uBDuR(x):
    W_M1 = 0
    while (W_M1 in range(0, 1)):
        W_M1 += 1
        with open('/dev/null', 'r'):
            W_H1 = 0
            while (W_H1 in range(0, 1)):
                W_H1 += 1
                PyCall_1682152177_LnosU(x)
