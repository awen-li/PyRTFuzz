
import os
import astunparse
from .astop import *


#####################################################################################################
#####################################################################################################
source_def = \
"""
import io
import pickle

class Pickler(pickle.Pickler):
  def persistent_id(self, obj):
    val = super().persistent_id(obj)
    return val

Pickler(io.BytesIO()).dump(42)

"""

class AppGen ():
    def __init__ (self):
        pass

    def Gen (self):
        Ast = ast.parse(source_def)
        print ("=============   original source   =============\r\n")

        ap = AstOp ()
        ap.visit (Ast)


