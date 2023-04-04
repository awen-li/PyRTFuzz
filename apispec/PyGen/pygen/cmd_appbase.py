
# _*_ coding:utf-8 _*_
import random
import string
import astunparse
import ast
from ast import *
from .astop import *
from .debug import *

def LoopRange (Prefix='F_', MaxLoop=3):
    LoopRange = random.randint (1, MaxLoop)
    LoopVar = random.choice (string.ascii_letters)
    LoopVar = Prefix + LoopVar + str (LoopRange)
    return LoopVar, LoopRange


class PyAppBase(AstOp):
    Tmpt = ""

    def __init__(self):
        self.init = None
        self.api  = None
        self.excepts   = None
        self.criterion = None
        self.PyCode    = None
        self.Tmpt = PyAppBase.Tmpt

        self.FN     = 'PyAppBase'
        self.FNFunc = None
    
    def SetExeCode (self, ExeCode):
        self.PyCode = ExeCode
        if self.PyCode == None:
            super(PyAppBase, self).__init__(self.Tmpt)
        else:
            super(PyAppBase, self).__init__(self.PyCode)
    
    def SetUp (self, init, api, excepts):
        if self.PyCode != None:
            return
        self.init = init
        self.api  = api
        self.excepts = excepts

    def HasFUnit (self, node):
        App = astunparse.unparse(node)
        if App.find (self.FN) != -1:
            return True
        return False

    def op_insert_invocation (self, node, InitStmt, CallStmt):
        pyBase = node.body[0]
        DebugPrint (ast.dump (pyBase))
        if not isinstance (pyBase, For):
            print (ast.dump (pyBase))
            raise Exception("Warning: must be For stmt!")

        if self.IsBlankBody (pyBase.body):
            pyBase.body = InitStmt.body
        else:
            pyBase.body += InitStmt.body
        pyBase.body += CallStmt.body
        return node

    def op_functiondef (self, node):
        pass

    def op_module(self, node):
        if self.HasFUnit (node) == True:
            return node
          
        node = super().op_module (node)
        if self.FNFunc != None:
            node.body.append (self.FNFunc)
        return node
        
    def GenApp (self):
        
        if self.PyCode == None:
            self.criterion = self.GetWrapF ()
            if self.criterion == None:
                DebugPrint ("[GenApp] get the insert point fail!...")
                return
            
            self.criterion.View()
            DebugPrint ("GenApp -> api: " + str(self.init) + "  " + self.api.Expr)
            
            astApp = ast.parse(self.Tmpt)
            new = self.visit(astApp)
            
            DebugPrint (astunparse.unparse(new))
            self.pG.ShowPg ()
            return astunparse.unparse(new)
        else:
            # we need to wrap the input code
            self.criterion = self.GetMainNode ()
            self.criterion.View()

            astApp = ast.parse(self.PyCode)
            new = self.visit(astApp)

            DebugPrint (astunparse.unparse(new))
            return astunparse.unparse(new)
        
        

        