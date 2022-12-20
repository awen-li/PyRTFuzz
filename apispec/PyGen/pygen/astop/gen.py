
import os
import astunparse
from .astop import *
from .propgraph import *
from .apptmpt import *


pg_tempt_oo = \
"""
class demoCls:
    def __init__(self):
        pass

    def demoFunc0(self):
        pass

    def demoFunc1(self, PYF_ARG1):
        pass

def RunFuzzer (x):
    pass
"""

pg_tempt_pro = \
"""
def demoFunc0 ():
    pass

def demoFunc1 (PYF_ARG1):
    pass

def RunFuzzer (x):
    pass
"""

pg_for = \
"""
for PYF_I in range (0, PYF_E):
    pass
"""

pg_inherit = \
"""
import io
import pickle

class Pickler(pickle.Pickler):
  def persistent_id(self, obj):
    return super().persistent_id(obj)

Pickler(io.BytesIO()).dump(42)
"""

#####################################################################################################
#####################################################################################################

class AppGen ():
    def __init__ (self):
        pass

    def Gen (self):
        Ast = ast.parse(pg_inherit)
        print ("=============   original source   =============\r\n")

        ap = AstOp ()
        ap.visit (Ast)

        for app in ATs.TmptList:
            pG = PropGraph ()
            pG.Build (app)

        


