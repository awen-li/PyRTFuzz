
import os
from ast import parse
from .astwalk import AstWalk
from xml.dom.minidom import Document

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

    def SetNodeAttr (self, node, name, value):
        node.setAttribute(name, value)
    
    def AddChild (self, Doc, Parent, Child, Value=None):
        CNode = Doc.createElement(Child)
        Parent.appendChild(CNode)
        if Value != None:
            Val = Doc.createTextNode(Value)
            CNode.appendChild(Val)
        return CNode
    
    def WriteXml (self, Visitor):
        Root = Document()  
        ApiSpec = self.AddChild (Root, Root, 'apisepc')
        ApiSpec.setAttribute ('version', '1.0')

        TotalApiNum   = 0
        TotalClassNum = 0
        TotalLibNum   = len (Visitor.pyLibs)
        for lib in Visitor.pyLibs:
            libNode = self.AddChild (Root, ApiSpec, "library")
            libNode.setAttribute ('name', lib.Name)
            
            for mdname, md in lib.Modules.items ():
                mdNode = self.AddChild (Root, libNode, 'module')
                mdNode.setAttribute ('name', mdname)

                TotalClassNum += len (md.Classes)
                for clsname, cls in md.Classes.items ():
                    clsNode = self.AddChild (Root, mdNode, "class")
                    clsNode.setAttribute ('name', clsname)
                    clsNode.setAttribute ('init', 'None')

                    TotalApiNum += len (cls.Apis)
                    for apiname, api in cls.Apis.items ():
                        apiNode = self.AddChild (Root, clsNode, "api")
                        apiNode.setAttribute ('name', apiname)

                        self.AddChild (Root, apiNode, "expr", str(api.Expr))
                        self.AddChild (Root, apiNode, "args", str(api.Args))
                        self.AddChild (Root, apiNode, "return", str(api.Ret))
                        self.AddChild (Root, apiNode, "dependences", str(api.Deps))
                        self.AddChild (Root, apiNode, "posargs", str(api.PosArgs))
                        self.AddChild (Root, apiNode, "kwoargs", str(api.KwoArgs))
                        
                        self.AddChild (Root, apiNode, "defa", str(api.Defaults))
                        self.AddChild (Root, apiNode, "kwodefa", str(api.KwDefaults))

                TotalApiNum += len (md.Apis)
                for apiname, api in md.Apis.items ():
                    print ("### API: " + apiname)
        
        with open ('apispec.xml', 'w') as af:
            af.write(Root.toprettyxml(indent="  "))
            af.close()

        print ("\n\n##### COLLECT: lib:%u, class:%u, api:%u #####\n\n" %(TotalLibNum, TotalClassNum, TotalApiNum))
        
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
                    if Ext != ".py" or Mod[0:1] == '_' or Path.find ("test") != -1:
                        continue

                    print ("## start proc mod: " + Mod)
                    Visitor.SetPyMod(Mod)
                    PyFile = os.path.join(Path, py)
                    with open(PyFile) as PyF:
                        print ("#visit " + PyFile)
                        Ast = parse(PyF.read(), PyFile, 'exec')
                        
                        Visitor.visit(Ast)

        #self.ShowSpec (Visitor)
        self.WriteXml (Visitor)
                
