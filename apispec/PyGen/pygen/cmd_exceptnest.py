
# _*_ coding:utf-8 _*_
import astunparse
import ast
from ast import *
from .cmd_appbase import *

class PyExceptNest(PyAppBase):
    def __init__(self):
        super(PyExceptNest, self).__init__()
        self.FN = 'ExceptNest'

    def op_try(self, node):
        Handlers = node.handlers[0]
        Handlers.body = [self.op_new_raise('e')]
        return node
    
    def op_functiondef (self, node):
        if node.name != self.criterion.Name:
            for st in node.body:
                self.visit (st)
            return node

        fp = self.criterion.NodeVal.Val
        RcCall = self.op_new_expr (self.op_new_call (self.FN, None, [fp[0]]))

        self.FNFunc = self.op_new_functiondef(self.FN, [fp[0]])
        self.FNFunc.body = self.op_try_wrapper (node.body, ['Exception'])

        node.body = [RcCall]
        return node

    

        