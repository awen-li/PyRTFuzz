
import os
from ast import parse
from .astwalk import AstWalk
from xml.dom.minidom import Document

class ApiSpecCheck ():
    def __init__ (self, ApiSpec='apispec.xml'):
        self.CodeDir = CodeDir

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

    @staticmethod 
    def SetNodeAttr (node, name, value):
        node.setAttribute(name, value)

    @staticmethod 
    def AddChild (Doc, Parent, Child, Value=None):
        CNode = Doc.createElement(Child)
        Parent.appendChild(CNode)
        if Value != None:
            Val = Doc.createTextNode(Value)
            CNode.appendChild(Val)
        return CNode

    @staticmethod 
    def WriteApi (Root, apiNode, api):
        ApiSpecGen.AddChild (Root, apiNode, "expr", str(api.Expr))
        ApiSpecGen.AddChild (Root, apiNode, "args", str(api.Args))
        ApiSpecGen.AddChild (Root, apiNode, "return", str(api.Ret))
        ApiSpecGen.AddChild (Root, apiNode, "dependences", str(api.Deps))
        ApiSpecGen.AddChild (Root, apiNode, "posargs", str(api.PosArgs))
        ApiSpecGen.AddChild (Root, apiNode, "kwoargs", str(api.KwoArgs))
                        
        ApiSpecGen.AddChild (Root, apiNode, "defa", str(api.Defas))
        ApiSpecGen.AddChild (Root, apiNode, "kwodefa", str(api.KwoDefas))
    
    @staticmethod     
    def WriteXml (pyLibs, ApiSpecXml='apispec.xml'):
        Root = Document()  
        ApiSpec = ApiSpecGen.AddChild (Root, Root, 'apisepc')
        ApiSpec.setAttribute ('version', '1.0')

        TotalApiNum   = 0
        TotalClassNum = 0
        TotalLibNum   = len (pyLibs)
        for lib in pyLibs:
            libNode = ApiSpecGen.AddChild (Root, ApiSpec, "library")
            libNode.setAttribute ('name', lib.Name)
            
            for mdname, md in lib.Modules.items ():
                mdNode = ApiSpecGen.AddChild (Root, libNode, 'module')
                mdNode.setAttribute ('name', mdname)

                TotalClassNum += len (md.Classes)
                for clsname, cls in md.Classes.items ():
                    clsNode = ApiSpecGen.AddChild (Root, mdNode, "class")
                    clsNode.setAttribute ('name', clsname)
                    clsNode.setAttribute ('init', 'None')

                    TotalApiNum += len (cls.Apis)
                    for apiname, api in cls.Apis.items ():
                        apiNode = ApiSpecGen.AddChild (Root, clsNode, "api")
                        apiNode.setAttribute ('name', apiname)
                        ApiSpecGen.WriteApi (Root, apiNode, api)
                        
                TotalApiNum += len (md.Apis)
                for apiname, api in md.Apis.items ():
                    apiNode = ApiSpecGen.AddChild (Root, mdNode, "api")
                    apiNode.setAttribute ('name', apiname)
                    ApiSpecGen.WriteApi (Root, apiNode, api)
        
        with open (ApiSpecXml, 'w') as af:
            af.write(Root.toprettyxml(indent="  "))
            af.close()

        print ("\n\n##### COLLECT: lib:%u, class:%u, api:%u #####\n\n" %(TotalLibNum, TotalClassNum, TotalApiNum))

    def GetModName (self, libName, PyFile, Mod):
        if libName == '.':
            return Mod
        
        Suffix = PyFile.find (libName)
        if Suffix == -1:
            raise Exception(PyFile + " find lib fail -> " + libName)
        Suffix += len (libName) + 1

        ModName, Ext = PyFile[Suffix:].split ('.')
        if Ext != 'py':
            raise Exception("Unsuport ext: " + Ext)
            
        ModName = ModName.replace ('/', '.')
        return ModName
    
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

                    PyFile = os.path.join(Path, py)           
                    ModName = self.GetModName (lib, PyFile, Mod)
                    Visitor.SetPyMod(ModName)
                    print ("## start proc mod: " + ModName)
                    
                    with open(PyFile) as PyF:
                        print ("#visit " + PyFile)
                        Ast = parse(PyF.read(), PyFile, 'exec')
                        
                        Visitor.visit(Ast)

        #self.ShowSpec (Visitor)
        ApiSpecGen.WriteXml (Visitor.pyLibs)
                
