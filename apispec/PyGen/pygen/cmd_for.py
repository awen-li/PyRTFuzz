
# _*_ coding:utf-8 _*_
import random
import string
import astunparse
import ast
from ast import *
from .astop import *
from .debug import *

def LoopRange (Prefix='F_', MaxLoop=6):
    LoopRange = random.randint (1, MaxLoop)
    LoopVar = random.choice (string.ascii_letters)
    LoopVar = Prefix + LoopVar + str (LoopRange)

    return LoopVar, LoopRange

class PyFor(AstOp):
    LoopVar, LoopRange = LoopRange ()   
    Tmpt = \
f"""
def demoFunc(arg):
    for {LoopVar} in range (0, {LoopRange}):
        pass

def RunFuzzer (x):
    demoFunc (x)
"""
    def __init__(self):
        self.init = None
        self.api  = None
        self.excepts   = None
        self.criterion = None
        self.PyCode    = None
        self.Tmpt = PyFor.Tmpt
    
    def SetExeCode (self, ExeCode):
        self.PyCode = ExeCode
        if self.PyCode == None:
            super(PyFor, self).__init__(self.Tmpt)
        else:
            super(PyFor, self).__init__(self.PyCode)
    
    def SetUp (self, init, api, excepts):
        if self.PyCode != None:
            return
        self.init = init
        self.api  = api
        self.excepts = excepts

    def op_insert_invocation (self, node, InitStmt, CallStmt):
        pyFor = node.body[0]
        DebugPrint (ast.dump (pyFor))
        if not isinstance (pyFor, For):
            print (ast.dump (pyFor))
            raise Exception("Warning: must be For stmt!")

        if self.IsBlankBody (pyFor.body):
            pyFor.body = InitStmt.body
        else:
            pyFor.body += InitStmt.body
        pyFor.body += CallStmt.body
        return node

    def op_functiondef (self, node):
        if node.name != self.criterion.Name:
            return node

        Var, Range = LoopRange ()
        forAst = ast.parse (f'for {Var} in range (0, {Range}):\
        pass').body[0]

        forAst.body = node.body
        node.body = [forAst]
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
        
        

        