
# _*_ coding:utf-8 _*_

import re
import ast
from ast import *

class ClassOp(NodeTransformer):
    def __init__(self, ClsName, FuncAst):
        self.ClsName = ClsName
        self.FuncAst = FuncAst

    def visit(self, node):
        if node is None:
            return

        method = 'op_' + node.__class__.__name__.lower()
        print (method)
        
        operator = getattr(self, method, self.generic_visit)
        print (operator)
        
        return operator(node)

    def new_function (self):
        pass

    def op_classdef(self, node):
        if self.ClsName != node.name:
            return

        classdef = ClassDef(name=node.name,
                            bases=node.bases,
                            keywords=node.keywords,
                            body=node.body)

        ClsBody = node.body
        for s in ClsBody:
            print (ast.dump (s))
            