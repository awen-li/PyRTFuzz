
import os
from ast import parse
from .astwalk import AstWalk 

class ApiSpec ():
    def __init__ (self, CodeDir):
        self.CodeDir = CodeDir

        self.Except = ['__pycache__', 'test', 'site-packages']

    def IsExcept (self, Path):
        for excp in self.Except:
            if Path.find (excp) != -1:
                return True
        return False
    
    def GenSpec (self):
        PyDirs = os.walk(self.CodeDir) 
        for Path, Dirs, Pys in PyDirs:
            if self.IsExcept (Path) == True:
                continue
            
            for py in Pys:
                _, Ext = os.path.splitext(py)
                if Ext != ".py":
                    continue
                
                PyFile = os.path.join(Path, py)
                print (PyFile)
                
                with open(PyFile) as PyF:
                    print ("#visit " + PyFile)
                    Ast = parse(PyF.read(), PyFile, 'exec')
                    Visitor = AstWalk()
                    Visitor.visit(Ast)
                break
                
            break