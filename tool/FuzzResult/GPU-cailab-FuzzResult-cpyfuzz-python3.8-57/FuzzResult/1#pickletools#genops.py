from fuzzwrap import PyDecode 
from pickletools import *
import pickletools
import argparse
import io
import pickle
import re
from pickle import decode_long

API_TYPE_LIST = ['bytes']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            pickle = PyDecode(API_TYPE_LIST, arg)
            ret = pickletools.genops(pickle)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, pickle.PickleError, pickle.PicklingError, pickle.UnpicklingError) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)
