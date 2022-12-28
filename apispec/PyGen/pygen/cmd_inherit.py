
# _*_ coding:utf-8 _*_
import random
import string
import astunparse
import ast
from ast import *
from .astop import *
from .debug import *

class PyInherit(AstOp):

    def __init__(self):
    	super(PyFor, self).__init__(PyFor.ForTmpt)
        self.init = None
        self.api  = None
        self.excepts   = None
        self.criterion = None
    
    def SetUp (self, init, api, excepts):
        if self.PyCode != None:
            return
        self.init = init
        self.api  = api
        self.excepts = excepts
        
    def GenApp (self):
        
        self.criterion = self.GetWrapF ()
        if self.criterion == None:
            DebugPrint ("[GenApp] get the insert point fail!...")
            return
            
        self.criterion.View()
        DebugPrint ("GenApp -> api: " + self.init + "  " + self.api.Expr)
            
        astApp = ast.parse(PyFor.ForTmpt)
        new = self.visit(astApp)
            
        DebugPrint (astunparse.unparse(new))
        self.pG.ShowPg ()
        return astunparse.unparse(new)

        
        

        