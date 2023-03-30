# _*_ coding:utf-8 _*_
import astunparse
import ast
from ast import *
from .cmd_appbase import *

class PyPrint(PyAppBase):
    Tmpt = ""\
"""
def PyPrint(obj):
    with open ("/dev/null", "w") as F:
        print (obj, file=F)
"""""
    def __init__(self):
        super(PyPrint, self).__init__()
        self.FN = 'PyPrint'

    def op_try(self, node):
        Obj = 'obj'
        if astunparse.unparse(node).find (Obj) == -1:
            return node
        
        PrintCall = self.op_new_expr (self.op_new_call (self.FN, None, [Obj]))
        node.body.append (PrintCall)

        self.FNFunc = ast.parse (PyPrint.Tmpt)
        return node
    
    def op_functiondef (self, node):
        if node.name != 'demoFunc':
            return node
        
        for st in node.body:
            self.visit (st)

        return node
        