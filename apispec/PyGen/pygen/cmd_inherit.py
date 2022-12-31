
# _*_ coding:utf-8 _*_
import random
import string
import astunparse
import ast
from ast import *
from .astop import *
from .debug import *

class PyInherit(AstOp):
    Tmpt =\
    """
import io
import pickle

class Pickler(pickle.Pickler):
  def persistent_id(self, obj):
    return super().persistent_id(obj)

def RunFuzzer (x):
    iob = io.BytesIO()
    ob  = Pickler(iob)
    ob.dump(x)
    """
    
    def __init__(self):
        super(PyInherit, self).__init__(PyInherit.Tmpt)
        self.init = None
        self.api  = None
        self.excepts   = None
        self.criterion = None
    
    def SetUp (self, init, api, excepts, cls=None):
        self.cls  = cls
        self.init = init
        self.api  = api
        self.excepts = excepts

    def op_base (self, base):
        if isinstance(base, Attribute):            
            print (ast.dump (base))
        elif isinstance(base, Name):
            print (ast.dump (base))
        else:
            print (ast.dump (base))
            raise Exception("op_base -> Unsupport!!!")

    def op_classdef(self, node):
        print (ast.dump (node), end="\n\n")

        bases = node.bases
        for base in bases:
            self.op_base (base)
        return node
        
        for st in node.body:
            self.visit (st)
        return node
        
    def GenApp (self):

        astApp = ast.parse(PyInherit.Tmpt)
        new = self.visit(astApp)
            
        DebugPrint (astunparse.unparse(new))
        self.pG.ShowPg ()
        return astunparse.unparse(new)

        
        

        