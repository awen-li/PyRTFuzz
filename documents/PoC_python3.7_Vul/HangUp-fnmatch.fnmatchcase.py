
from fnmatch import *
import fnmatch
import re

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, name, pat):
        try:
            ret = fnmatch.fnmatchcase(name, pat)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
            pass

with open ("fnmatch.fnmatchcase-name", "r") as F:
    name = F.read ()
                
with open ("fnmatch.fnmatchcase-pat", "r") as F:
    pat = F.read ()
                
dc = demoCls()
dc.demoFunc(name, pat)
