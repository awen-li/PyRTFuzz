# _*_ coding:utf-8 _*_
import astunparse
import ast
from ast import *
from .cmd_appbase import *

class PyIf(PyAppBase):
    Tmpt = \
f"""
def demoFunc(arg):
    if True:
        pass

def RunFuzzer (x):
    demoFunc (x)
"""
    def __init__(self):
        super(PyIf, self).__init__()
        self.Tmpt = PyIf.Tmpt

    def op_functiondef (self, node):
        if node.name != self.criterion.Name:
            return node

        IfAst = ast.parse ('if True:\
        pass').body[0]

        IfAst.body = node.body
        node.body = [IfAst]
        return node
        
        