
# _*_ coding:utf-8 _*_
import random
import string
import astunparse
import ast
from ast import *
from .cmd_for import *
from .debug import *

class PyWhile(PyFor):
    LoopVar, LoopRange = LoopRange (Prefix='W_') 
    Tmpt = \
f"""
def demoFunc(arg):
    {LoopVar} = 0
    while {LoopVar} in range (0, {LoopRange}):
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
        self.Tmpt = PyWhile.Tmpt

    def op_functiondef (self, node):
        if node.name != self.criterion.Name:
            return node

        Var, Range = LoopRange (Prefix='W_') 

        InitAst  = ast.parse (f'{Var} = 0').body[0]
        WhileAst = ast.parse (f'while {Var} in range (0, {Range}):\
        pass').body[0]

        WhileAst.body = node.body
        node.body = [InitAst, WhileAst]
        return node
        
        