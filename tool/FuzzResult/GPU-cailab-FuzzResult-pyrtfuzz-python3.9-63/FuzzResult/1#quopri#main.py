from fuzzwrap import PyDecode 
from quopri import *
import quopri
import getopt
from io import BytesIO

API_TYPE_LIST = []

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            quopri.main()
        except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError, getopt.GetoptError, getopt.error) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)
