from fuzzwrap import PyDecode 
from json.tool import *
import json
import argparse
import json.tool

API_TYPE_LIST = []

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            json.tool.main()
        except (AssertionError, AttributeError, BrokenPipeError, LookupError, OSError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)
