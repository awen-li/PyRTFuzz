from fuzzwrap import PyDecode 
from webbrowser import *
import webbrowser
import copy
import getopt
import shutil
import subprocess
import threading

API_TYPE_LIST = ['str', 'type', 'ExampleBrowser']

def demoFunc(arg):
    try:
        (name, klass, instance) = PyDecode(API_TYPE_LIST, arg)
        webbrowser.register(name, klass, instance)
    except (AssertionError, AttributeError, FileNotFoundError, KeyError, LookupError, NotADirectoryError, NotImplementedError, OSError, PermissionError, TypeError, ValueError, copy.Error, getopt.GetoptError, getopt.error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError, subprocess.TimeoutExpired, threading.BrokenBarrierError, webbrowser.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        PyCall_1682122868_lCvuZ(x)

def PyCall_1682122868_IrMws(x):
    for F_w1 in range(0, 1):
        W_e1 = 0
        while (W_e1 in range(0, 1)):
            W_e1 += 1
            demoFunc(x)

def PyCall_1682122868_lCvuZ(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            W_J1 = 0
            while (W_J1 in range(0, 1)):
                W_J1 += 1
                W_e1 = 0
                while (W_e1 in range(0, 1)):
                    W_e1 += 1
                    with open('/dev/null', 'r'):
                        W_X1 = 0
                        while (W_X1 in range(0, 1)):
                            W_X1 += 1
                            for F_v1 in range(0, 1):
                                PyCall_1682122868_IrMws(x)
