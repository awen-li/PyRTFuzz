
import os
import re
from progressbar import ProgressBar
from pyspec import *
from .cmd_newoo import *
from .cmd_newpo import *
from .cmd_inherit import *
from .cmd_import import *
from .cmd_for import *
from .cmd_while import *
from .cmd_with import *
from .cmd_if import *
from .cmd_call import *
from .cmd_recursive import *
from .cmd_exceptnest import *
from .cmd_print import *
from .cmd_repr import *
from .debug import *

class ApiInfo ():
    def __init__ (self, Module, ClsInit, Cls, Api, Exceps):
        self.Module  = Module
        self.ClsInit = ClsInit
        self.Class   = Cls
        self.Api     = Api
        self.Exceps  = Exceps
        self.Weight  = 1
            
class SLCmd ():
    BASE = 1
    APP  = 2

    NestNone   = 0
    NestCmd    = 1
    NestBrkCmd = 2
    
    def __init__ (self, CmdName, Module, Type, OORequired=False, Mod=1, Nested=NestNone):
        self.CmdName = CmdName
        self.Module  = Module
        self.Type    = Type
        self.OORequired = OORequired
        self.Mod     = Mod
        self.Nested  = Nested

class CmdOP ():
    def __init__ (self, OpName):
        self.OpName = OpName


class ExeCmd ():
    def __init__ (self, Cmd, SlCmd, Para):
        self.Cmd   = Cmd
        self.SlCmd = SlCmd
        self.Para  = Para

class Core ():
    def __init__ (self, apiSpecXml=None):
        self.PyLibs  = self.InitPyLibs (apiSpecXml)
        self.ApiList   = {}
        self.ClassInfo = {}
        self.ModuleList= {}
        self.InitApiList ()
        
        self.CmdList = {}
        self.OpList  = {}
        self.InitCmd ()

        self.RunStack = []
        self.LocalValue = {}
        self.ExeModule = None

        self.InitOk = bool(len (self.PyLibs) != 0)

    def ShowCmds (self):
        print ("\n############## SL Interpreter Statement List [%2d] ##############" %len (self.CmdList))
        for Cmd, CmdObj in self.CmdList.items ():
            print ("### %-12s ---- %-16s" %(Cmd, CmdObj.CmdName))
        print ("###################################################################\n")

    def InitApiList (self):
        if len (self.PyLibs) == 0:
            return
        
        par = ProgressBar ()
        for libName, pyLib in par(self.PyLibs.items ()):
            for mdName, pyMoudle in pyLib.Modules.items ():
                MdExcepts = [e.exName for e in pyMoudle.Exceptions]
                self.ModuleList [mdName] = pyMoudle
                
                for clsName, cls in pyMoudle.Classes.items ():
                    for apiName, api in cls.Apis.items ():
                        if apiName == '__init__':
                            continue

                        absPath = mdName + '.' + clsName + '.' + apiName
                        ClsInit = cls.clsInit
                        if ClsInit == 'None':
                            ClsInit = None
                        apiInfo = ApiInfo (pyMoudle, ClsInit, clsName, api, MdExcepts)
                        self.ApiList[absPath] = apiInfo
                    self.ClassInfo [clsName] = cls

                for apiName, api in pyMoudle.Apis.items ():
                    absPath = mdName + '.' + apiName
                    self.ApiList[absPath] = ApiInfo (pyMoudle, None, None, api, MdExcepts)
        DebugPrint ("Load API number: " + str (len (self.ApiList)))
                    
    def Push (self, Var, Value):
        self.RunStack.append (Var)
        self.LocalValue [Var] = Value

    def Pop (self):
        Var = self.RunStack.pop ()
        Value = self.LocalValue.pop (Var)
        return Var, Value

    def GetVarValue (self, Var):
        return self.LocalValue.get (Var)

    def InitPyLibs (self, apiSpecXml):
        apiSpec = ApiSpecLoader (apiSpecXml)
        apiSpec.Parser ()
        return apiSpec.PyLibs

    def GetApiInfo (self, testApi):
        return self.ApiList.get (testApi)

    def GetCmdList (self):
        return self.CmdList

    def InitCmd (self):
        self.CmdList['OO']  = SLCmd ('NewOO ()', 'cmd_newoo', SLCmd.BASE)
        self.CmdList['PO']  = SLCmd ('NewPO ()', 'cmd_newpo', SLCmd.BASE)
        self.CmdList['Inherit'] = SLCmd ('PyInherit ()', 'cmd_inherit', SLCmd.BASE, OORequired=True)
        
        self.CmdList['For'] = SLCmd ('PyFor ()', 'cmd_for', SLCmd.APP, Mod=2, Nested=SLCmd.NestCmd)
        self.CmdList['While'] = SLCmd ('PyWhile ()', 'cmd_while', SLCmd.APP, Mod=2, Nested=SLCmd.NestCmd)
        self.CmdList['Wtih'] = SLCmd ('PyWith ()', 'cmd_with', SLCmd.APP, Nested=SLCmd.NestCmd)
        self.CmdList['If'] = SLCmd ('PyIf ()', 'cmd_if', SLCmd.APP, Nested=SLCmd.NestCmd)
        self.CmdList['Call'] = SLCmd ('PyCall ()', 'cmd_call', SLCmd.APP, Nested=SLCmd.NestBrkCmd)
        self.CmdList['Print'] = SLCmd ('PyPrint ()', 'cmd_print', SLCmd.APP)
        self.CmdList['Repr'] = SLCmd ('PyRepr ()', 'cmd_repr', SLCmd.APP)

        #self.CmdList['Recursive'] = SLCmd ('PyRecursive ()', 'cmd_recursive', SLCmd.APP, Mod=3)
        #self.CmdList['ExceptNest'] = SLCmd ('PyExceptNest ()', 'cmd_exceptnest', SLCmd.APP, Mod=4)

    def GetSlCmd (self, CmdName):
        return self.CmdList.get (CmdName)

    def DeCmd (self, Stmt):
        Cmd = re.findall (r"^(.+?)\(", Stmt)
        if len (Cmd) == 0:
            raise Exception("No cmd in " + Stmt)
        Cmd = Cmd [0].strip ()
        return Cmd

    def DePara (self, Stmt):
        Para = re.findall (r"\((.+?)\)", Stmt)
        if len (Para) == 0:
            raise Exception("No parameter in " + Stmt)
        Para = Para[0].strip ()
        return Para

    def Decode (self, Cmd):
        val = Cmd.split ('=')
        if len (val) == 0:
            raise Exception("No execution info in cmd")

        Var = Stmt = None
        if len (val) == 1:
            Stmt = val [0].strip ()         
        else:
            Var  = val [0].strip ()
            Stmt = val [1].strip ()

        Cmd = self.DeCmd (Stmt)
        Para = self.DePara(Stmt)
        SlCmd = self.GetSlCmd(Cmd)
        if SlCmd == None:
            raise Exception("Not support current cmd -> " + Cmd)

        return Var, ExeCmd (Cmd, SlCmd, Para)

    def Exe (self, exeCmd):
        SlCmd = exeCmd.SlCmd
        DebugPrint ("Local value:" + str(self.LocalValue))

        DebugPrint ("@@@@ Exe -> " + exeCmd.Cmd + " to " + SlCmd.CmdName + " with " + exeCmd.Para)
        Value = self.GetVarValue (exeCmd.Para)
        if Value != None:
            Var, Val = self.Pop ()
            if Var != exeCmd.Para:
                raise Exception("Inconsistency with stack: " + Var + " -> " + exeCmd.Para)
            
            ExeCode = Value
            ExeObj = eval (SlCmd.CmdName)
            ExeObj.SetExeCode (ExeCode)
        else:
            ExeCode = self.GetApiInfo (exeCmd.Para)
            if ExeCode == None:
                raise Exception("Get tested api fail: " + exeCmd.Para)
            
            #cache for import
            self.ExeModule = ExeCode.Module
            
            ExeObj = eval (SlCmd.CmdName)      
            ExeObj.SetUp (ExeCode.ClsInit, ExeCode.Api, ExeCode.Exceps, ExeCode.Class)
            if hasattr (ExeObj, 'SetClass') == True:
                clsInfo = self.ClassInfo.get (ExeCode.Class)
                if clsInfo == None:
                    raise Exception(ExeCode.Class + " has no attributes")
                ExeObj.SetClass (clsInfo)
            
        return ExeObj.GenApp ()

    def RunImport (self, App):
        if self.ExeModule == None:
            raise Exception("Fail to obtain current executed module!")

        PyImpt = PyImport (self.ExeModule)
        App = PyImpt.GenImport (App) + App
        self.ExeModule = None
        return App

    def Write(self, App, OutPut):
        with open (OutPut, "w") as pyApp:
            pyApp.write (App)
  
    def Run (self, Script, OutPut='pyapp.py'):
        DebugPrint ("Start run script: " + Script + '\r\n')
        Script = Script.split ('\n')
        for cmd in Script:
            cmd = cmd.strip ()
            if cmd == '':
                continue

            Var, exeCmd = self.Decode (cmd)
            Value = self.Exe (exeCmd)
            if Value == None:
                raise Exception("Exe fail: " + cmd)

            if Var != None:
                self.Push (Var, Value)
            else:
                self.Push ('Default', Value)
            
        
        Var, App = self.Pop ()
        App = self.RunImport (App)
        DebugPrint (App)
        self.Write (App, OutPut)

