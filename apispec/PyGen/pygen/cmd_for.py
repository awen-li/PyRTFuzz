
# _*_ coding:utf-8 _*_
import astunparse
import ast
from ast import *
from .cmd_appbase import *

class PyFor(PyAppBase):
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
        super(PyFor, self).__init__()
        self.Tmpt = PyFor.Tmpt

    def op_functiondef (self, node):
        if node.name != self.criterion.Name:
            return node

        Var, Range = LoopRange ()
        forAst = ast.parse (f'for {Var} in range (0, {Range}):\
        pass').body[0]

        forAst.body = node.body
        node.body = [forAst]
        return node

        
        

        