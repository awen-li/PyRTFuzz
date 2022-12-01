#!/usr/bin/python

import os
from ast import parse
from .AstWalk import AstWalk

def ParsePyFile (PyDir):

    PyDirs = os.walk(PyDir) 
    for Path, Dirs, Pys in PyDirs:
        for py in Pys:
            _, Ext = os.path.splitext(py)
            if Ext != ".py":
                continue
            
            PyFile = os.path.join(Path, py)
            with open(PyFile) as PyF:
                print ("#visit " + PyFile)
                Ast = parse(PyF.read(), PyFile, 'exec')
                Visitor = AstWalk()
                Visitor.visit(Ast) 