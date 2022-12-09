
# _*_ coding:utf-8 _*_

import re
import ast
from ast import *


class AstOp (NodeTransformer):
    def __init__(self):
        pass

    def visit(self, node):
        if node is None:
            return

        method = 'op_' + node.__class__.__name__.lower()
        operator = getattr(self, method, self.generic_visit)        
        return operator(node)

    def get_arg (self, node, index=1):
        args  = node.args.args
        argno = 0
        for arg in args:
            if argno == index:
                return Name(id=arg.arg, ctx=Load())
            argno += 1
        return None


class ClassOp(AstOp):
    def __init__(self, ClsName, FuncAst, Op):
        super(AstOp, self).__init__()
        self.ClsName = ClsName
        self.FuncAst = FuncAst
        self.Op      = Op

    def op_functiondef (self, node):
        if node.name != 'demoFunc1':
            return node

        arg = self.get_arg (node)
        callee = self.FuncAst.body[0].value
        callee.args = [arg]
        
        node.body = self.FuncAst.body
        return node

    def op_classdef(self, node):
        if self.ClsName != node.name:
            return

        if self.Op == 'INSERT_CALL':
            for st in node.body:
                self.visit (st)
        
        return node


class FuncOp(AstOp):
    def __init__(self, FuncName, UnitAst, Op):
        super(AstOp, self).__init__()
        self.UnitAst = UnitAst
        self.FuncName = FuncName
        self.Op = Op

    def op_for (self, node, argS, argE):
        if isinstance (node.iter, Call):
            callee = node.iter
            if callee.func.id == 'range':
                callee.args = [argS, argE]
        return node
    
    def op_functiondef (self, node):
        if node.name != self.FuncName:
            return node

        if self.Op == 'INSERT_FOR':
            forAst = self.op_for (self.UnitAst.body[0], Constant(value=0), self.get_arg(node))

            oldBody = node.body
            forAst = self.UnitAst.body[0]

            oldBody[0].value.args = [forAst.target]
            forAst.body = oldBody
            
            node.body = self.UnitAst.body

        elif self.Op == 'INSERT_ENTRY':
            enAst = self.UnitAst.body[0]
            node.body = self.UnitAst.body + node.body
        
        return node

            