# _*_ coding:utf-8 _*_
import astunparse
import ast
from ast import *
from .cmd_appbase import *

class PyRepr(PyAppBase):
    Tmpt = ""

    def __init__(self):
        super(PyRepr, self).__init__()

    def op_try(self, node):
        Obj = 'obj'
        Stmts = astunparse.unparse(node)
        if Stmts.find (Obj) == -1 or Stmts.find ('repr') != -1:
            return node

        ReprCall = self.op_new_expr (self.op_new_call ('repr', None, [Obj]))
        node.body.append (ReprCall)

        return node
    
    def op_functiondef (self, node):
        if node.name != 'demoFunc':
            return node
        
        for st in node.body:
            self.visit (st)

        return node
        