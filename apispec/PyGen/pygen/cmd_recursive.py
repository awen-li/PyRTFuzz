
# _*_ coding:utf-8 _*_
import astunparse
import ast
from ast import *
from .cmd_appbase import *

class PyRecursive(PyAppBase):
    def __init__(self):
        self.RC = 'Recursive'
        self.RCFunc = None

    def HasRecursive (self, node):
        App = astunparse.unparse(node)
        if App.find (self.RC) != -1:
            return True
        return False
    
    def op_functiondef (self, node):
        if node.name != self.criterion.Name:
            return node
        
        if self.HasRecursive (node) == True:
            return node

        fp = self.criterion.NodeVal.Val
        RcCall = self.op_new_expr (self.op_new_call (self.RC, None, [fp[0]]))

        self.RCFunc = self.op_new_functiondef(self.RC, [fp[0]])
        self.RCFunc.body = node.body
        self.RCFunc.body.append (RcCall)

        node.body = [RcCall]
        return node
    
    def op_module(self, node):    
        node = super().op_module (node)
        if self.RCFunc != None:
            node.body.append (self.RCFunc)
        return node
    


        
        

        