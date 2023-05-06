
from operator import *
import operator

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, a):
        try:
            ret = operator.mod(a, 3777)
        except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
            print (e)

with open ("operator.mod-a", "r") as F:
    a = F.read ()
                
dc = demoCls()
dc.demoFunc(a)
