
from timeit import *
import timeit
import getopt
import time

def demoFunc(src, indent):
    try:
        #indent = 342221180806
        ret = timeit.reindent(src, indent)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, getopt.GetoptError, getopt.error) as e:
        pass


demoFunc ("", 64222118081)