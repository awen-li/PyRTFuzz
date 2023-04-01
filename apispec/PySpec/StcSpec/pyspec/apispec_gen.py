
import os
from ast import parse
from xml.dom.minidom import Document
from .astwalk import AstWalk
from .apispec import *
from platform import python_version

class ApiSpecGen ():
    def __init__ (self, CodeDir):
        self.CodeDir = CodeDir
        if self.CodeDir[-1] != '/':
            self.CodeDir += '/'

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
    def IsAbnormalExc (exc):
        if exc[0:1] == '_':
            return True
        
        if exc in ['ftplib.all_errors', 'BadUsage']:
            return True

        if exc.find ('.') != -1:
            block = exc.split ('.')
            md = block[0]
            if md in ['self', 's', 'source', 'd', 'header']:
                return True
            name = block[-1]
            if name[0:1] == '_':
                return True
        else:
            if exc.islower ():
                return True
        return False
    
    @staticmethod
    def RemoveRedundantExc (Exceptions):
        ExcList = []
        for exc in Exceptions:
            if ApiSpecGen.IsAbnormalExc (exc.exName):
                continue
            ExcList.append (exc.exName)
        ExcList = list (set (ExcList))

        OptList = []
        for exc in ExcList:
            SubFlag = False
            for exc2 in ExcList:
                if exc2 == exc:
                    continue
                if exc2.find ('.') == -1:
                    continue
                SubExcs = exc2.split ('.')
                if exc in SubExcs:
                    SubFlag = True
                    break
            if SubFlag == False:
                OptList.append (exc)
        OptList.sort ()
        return OptList

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
    def WriteErrs (Root, excpNode, excp):
        ApiSpecGen.AddChild (Root, excpNode, "exception", str(excp))

    @staticmethod     
    def GetSpecName (ApiSpecXml='apispec.xml'):
        if ApiSpecXml.find('CPY_') != -1:
            return ApiSpecXml
        return 'CPY_' + python_version() + '_' + ApiSpecXml
    
    @staticmethod     
    def WriteXml (pyLibs, ApiSpecXml='apispec.xml'):
        ApiSpecXml = ApiSpecGen.GetSpecName (ApiSpecXml)
        
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
                if IsExcept(mdname) == True:
                    continue
                md.Imports.sort ()
                md.ImportFrom.sort ()

                mdNode = ApiSpecGen.AddChild (Root, libNode, 'module')
                mdNode.setAttribute ('name', mdname)
                mdNode.setAttribute ('imports', str(md.Imports))
                mdNode.setAttribute ('importfrom', str(md.ImportFrom))

                for clsname, cls in md.Classes.items ():
                    if clsname[0:1] == '_':
                        continue
                    
                    TotalClassNum += 1
                    clsNode = ApiSpecGen.AddChild (Root, mdNode, "class")
                    clsNode.setAttribute ('name', clsname)
                    clsNode.setAttribute ('init', cls.clsInit)
                    if cls.Base != None:
                        clsNode.setAttribute ('base', cls.Base)

                    for apiname, api in cls.Apis.items ():
                        if apiname[0:1] == '_' and apiname != '__init__':
                            continue
                        
                        TotalApiNum += 1
                        apiNode = ApiSpecGen.AddChild (Root, clsNode, "api")
                        apiNode.setAttribute ('name', apiname)
                        ApiSpecGen.WriteApi (Root, apiNode, api)
                        
                for apiname, api in md.Apis.items ():
                    if apiname[0:1] == '_':
                        continue
                    
                    TotalApiNum += 1
                    apiNode = ApiSpecGen.AddChild (Root, mdNode, "api")
                    apiNode.setAttribute ('name', apiname)
                    ApiSpecGen.WriteApi (Root, apiNode, api)

                if len (md.Exceptions) != 0:
                    excepNode = ApiSpecGen.AddChild (Root, mdNode, "errors")
                    ExcList = ApiSpecGen.RemoveRedundantExc (md.Exceptions)
                    for excep in ExcList:
                        ApiSpecGen.WriteErrs (Root, excepNode, excep)
        
        with open (ApiSpecXml, 'w') as af:
            af.write(Root.toprettyxml(indent="  "))
            af.close()

        print ("\n\n##### COLLECT: lib:%u, class:%u, api:%u #####\n\n" %(TotalLibNum, TotalClassNum, TotalApiNum))

    def GetModName (self, libName, PyFile, Mod):
        ModFile = PyFile[len(self.CodeDir):]

        if libName == '.':
            ModFile = ModFile[2:]
            if ModFile.find ('/') != -1:
                return None
            return Mod

        ModName, Ext = ModFile.split ('.')
        ModName = ModName.replace ('/', '.')
        return ModName
    
    def GenSpec (self):
        AllLibs = self.GetLibs ()

        Visitor = AstWalk()  
        for lib in AllLibs:
            libDir = os.path.join(self.CodeDir, lib)
            if IsExcept (libDir) == True:
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
                    if IsExcept (PyFile) == True:
                        continue
                
                    ModName = self.GetModName (lib, PyFile, Mod)
                    if ModName == None:
                        continue
                    Visitor.SetPyMod(ModName)
                    print ("## start proc mod: " + ModName)
                    
                    with open(PyFile) as PyF:
                        print ("#visit " + PyFile)
                        Ast = parse(PyF.read(), PyFile, 'exec')         
                        Visitor.visit(Ast)
                        
        #self.ShowSpec (Visitor)
        ApiSpecGen.WriteXml (Visitor.pyLibs)
                
