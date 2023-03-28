# _*_ coding:utf-8 _*_
import astunparse
import ast
from ast import *
from .cmd_appbase import *

class PyWith(PyAppBase):
    Tmpt = \
f"""
def demoFunc(arg):
    with open ("/dev/null", "r"):
        pass

def RunFuzzer (x):
    demoFunc (x)
"""
    def __init__(self):
        self.Tmpt = PyWith.Tmpt

    def op_functiondef (self, node):
        if node.name != self.criterion.Name:
            return node

        WithAst = ast.parse ('with open ("/dev/null", "r"):\
        pass').body[0]

        WithAst.body = node.body
        node.body = [WithAst]
        return node
        
        