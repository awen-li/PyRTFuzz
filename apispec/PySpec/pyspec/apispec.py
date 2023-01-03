
import os
from ast import parse
from .astwalk import AstWalk 

class ApiSpec ():
    def __init__ (self, CodeDir):
        self.CodeDir = CodeDir

        self.Except = ['__pycache__', 'test', 'site-packages', 'sqlite3', 'distutils', 'importlib']

    def IsExcept (self, Path):
        for excp in self.Except:
            if Path.find (excp) != -1:
                return True
        return False

    def GetLibs (self):
        AllDirs = os.walk(self.CodeDir)
        for Path, Libs, Pys in AllDirs:
            Libs.append ('.')
            return Libs

    def ShowSpec (self, Visitor):
        print ("\n\n=========================== ShowSpec ===========================")
        for lib in Visitor.pyLibs:
            print ("# LIB: " + lib.Name)
            for mdname, md in lib.Modules.items ():
                print ("## MOD: " + mdname)
                for clsname, cls in md.Classes.items ():
                    print ("### CLASS: " + clsname)
                    for apiname, api in cls.Apis.items ():
                        print ("#### API: " + apiname)

                for apiname, api in md.Apis.items ():
                    print ("### API: " + apiname)
    
    def GenSpec (self):
        AllLibs = self.GetLibs ()

        Visitor = AstWalk()
        
        for lib in AllLibs:
            libDir = os.path.join(self.CodeDir, lib)
            if self.IsExcept (libDir) == True:
                continue

            Visitor.SetPyLib(lib)
            print ("# start proc lib: " + lib)
            ModDir = os.walk(libDir)
            for Path, Dirs, Pys in ModDir:      
                for py in Pys:
                    Mod, Ext = os.path.splitext(py)
                    if Ext != ".py" or Mod[0:1] == '_':
                        continue

                    print ("## start proc mod: " + Mod)
                    Visitor.SetPyMod(Mod)
                    PyFile = os.path.join(Path, py)
                    with open(PyFile) as PyF:
                        print ("#visit " + PyFile)
                        Ast = parse(PyF.read(), PyFile, 'exec')
                        
                        Visitor.visit(Ast)
                break
            break

        self.ShowSpec (Visitor)
                
