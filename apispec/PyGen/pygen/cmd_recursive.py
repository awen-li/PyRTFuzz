
# _*_ coding:utf-8 _*_
import astunparse
import random
import ast
from ast import *
from .cmd_appbase import *

class PyRecursive(PyAppBase):
    Tmpt = \
f"""
def demoFunc(arg):
    pass

def RunFuzzer (x):
    demoFunc (x)
"""
    def __init__(self):
        self.Tmpt = PyRecursive.Tmpt
        self.RC = 'Recursive'

    def HasRecursive (self, node):
        for st in node.body:
            if not isinstance (st, Call):
                continue
            if st.func.id == self.RC:
                return True
        return False
    
    def op_functiondef (self, node):
        if node.name != self.criterion.Name:
            return node
        
        if self.HasRecursive (node) == True:
            print ("Already in recursive!!!!!!!!!!!!!")
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
        node.body.append (self.RCFunc)
        return node
    


        
        

        