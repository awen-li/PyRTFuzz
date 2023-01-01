
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
class demoCls:
    def __init__(self):
        sp = super ()
        sp.__init__ ()

    def demoFunc1(self, arg1):
        pass

def RunFuzzer (x):
    ob = demoCls ()
    ob.demoFunc1 (x)
    """
    
    def __init__(self):
        super(PyInherit, self).__init__(PyInherit.Tmpt)
        self.cls  = None
        self.init = None
        self.api  = None
        self.excepts   = None
        self.criterion = None
        self.ovfunc    = None
    
    def SetUp (self, init, api, excepts, cls=None):
        self.cls  = cls
        self.init = init
        self.api  = api
        self.excepts = excepts

    def SetClass (self, pyClass):
        self.pyClass = pyClass
        print (self.pyClass)

    def op_new_base (self):
        if self.cls == None:
            raise Exception("op_base -> Unsupport without base class!!!")

        base = None
        cls = self.cls.split ('.')
        if len (cls) > 2:
            raise Exception("op_base -> Unsupport format " + self.cls)
        elif len (cls) == 2:
            base = self.op_new_attribute (cls[0], cls[1])
        else:
            base = self.op_new_value (cls[0])
    
        return [base]

    def op_functiondef (self, node):
        if self.ovfunc != None:
            if self.ovfunc.name == node.name:
                self.ovfunc = None
        return super ().op_functiondef (node)   
        
    def op_classdef(self, node):
        print (ast.dump (node), end="\n\n")

        # add base
        node.bases = self.op_new_base ()

        # override one function
        for apiName, api in self.pyClass.Apis.items ():
            print (apiName)
            print (api.Expr)
            print (api.Parameters)
            
            paras = [p.split(':')[0] for p in api.Parameters]
            self.ovfunc = self.op_new_functiondef (apiName, paras)
            node = super ().op_classdef (node)
            if self.ovfunc != None:
                self.ovfunc.body = [Pass()]
                node.body.append (self.ovfunc)
        return node

        
    def GenApp (self):

        astApp = ast.parse(PyInherit.Tmpt)
        new = self.visit(astApp)
            
        DebugPrint (astunparse.unparse(new))
        self.pG.ShowPg ()
        return astunparse.unparse(new)

        
        

        