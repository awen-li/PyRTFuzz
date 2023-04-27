from fuzzwrap import PyDecode 
from gzip import *
import gzip
import io

API_TYPE_LIST = []

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            gzip.main()
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, UnicodeEncodeError, ValueError, gzip.BadGzipFile) as e:
            pass

def RunFuzzer(x):
    if True:
        dc = demoCls()
        dc.demoFunc(x)
