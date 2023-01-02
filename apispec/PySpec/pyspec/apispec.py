
import os
from ast import parse
from .astwalk import AstWalk 

class ApiSpec ():
    def __init__ (self, CodeDir):
        self.CodeDir = CodeDir

    def GenSpec (self):
        PyDirs = os.walk(self.CodeDir) 
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