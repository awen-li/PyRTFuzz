
import ast
from ast import *
from .apptmpt import *

"""
Example:
class demoCls:
    def __init__(self):
        pass

    def demoFunc1(self, arg1):
        pass

def RunFuzzer (x):
    demoCls ().demoFunc1 (x)

-------------------------------------------------------------------
control flow graph:

               RunFuzzer (x)
                    |
          obj = demoCls.__init__()
                    |
             obj.demoFunc1 (x)

class graph:
                demoCls
                /     \
  __init__ (init)    demoFunc1 (x)
"""

class PgNode ():
    def __init__ (self):
        pass


class PgEdge ():
    def __init__ (self):
        pass

        
class PropGraph (NodeVisitor):
    def __init__ (self, MainFunc='RunFuzz'):
        self.MainFunc = MainFunc


    def Build (self):
        for tmpt in ATs.TmptList:
            print (tmpt)

