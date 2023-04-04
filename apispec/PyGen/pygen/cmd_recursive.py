
# _*_ coding:utf-8 _*_
import astunparse
import ast
from ast import *
from .cmd_appbase import *

class PyRecursive(PyAppBase):
    def __init__(self):
        super(PyRecursive, self).__init__()
        self.FN = 'Recursive'
    
    def op_functiondef (self, node):
        if node.name != self.criterion.Name:
            return node

        fp = self.criterion.NodeVal.Val
        RcCall = self.op_new_expr (self.op_new_call (self.FN, None, [fp[0]]))

        self.FNFunc = self.op_new_functiondef(self.FN, [fp[0]])
        self.FNFunc.body = node.body
        self.FNFunc.body.append (RcCall)

        ImportSys = self.op_new_import (['sys'])
        ExitCall = self.op_new_expr (self.op_new_call ("sys", "exit", []))
        node.body = self.op_try_wrapper ([RcCall], ['RecursionError'], [ImportSys, ExitCall]) 
        return node
    
    


        
        

        