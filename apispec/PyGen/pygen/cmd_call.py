
# _*_ coding:utf-8 _*_
import random
import string
import astunparse
import ast
from ast import *
from .cmd_appbase import *
import time

class PyCall(PyAppBase):
    def __init__(self):
        super(PyCall, self).__init__()
        self.FN = 'PyCall_' + str(int (time.time())) + '_' + self.GetRandomSuffix()
    
    def GetRandomSuffix (self, Len=5):
        Suffix = ""
        while Len > 0:
            Suffix += random.choice (string.ascii_letters)
            Len -= 1
        return Suffix
    
    def op_functiondef (self, node):
        if node.name != self.criterion.Name:
            return node

        fp = self.criterion.NodeVal.Val
        RcCall = self.op_new_expr (self.op_new_call (self.FN, None, [fp[0]]))

        self.FNFunc = self.op_new_functiondef(self.FN, [fp[0]])
        self.FNFunc.body = node.body

        node.body = [RcCall]
        return node
    
    


        
        

        