
import os
import re
from pyspec import *
from .cmd_newoo import *
from .cmd_newpo import *
from .cmd_for import *
from .cmd_inherit import *
from .debug import *

class ApiInfo ():
    def __init__ (self, ClsInit, Cls, Api, Exceps):
        self.ClsInit = ClsInit
        self.Class   = Cls
        self.Api     = Api
        self.Exceps  = Exceps
            
class SLCmd ():
    Level1 = 1
    Level2 = 2
    
    def __init__ (self, CmdName, Module, Level):
        self.CmdName = CmdName
        self.Module  = Module

class CmdOP ():
    def __init__ (self, OpName):
        self.OpName = OpName


class ExeCmd ():
    def __init__ (self, Cmd, SlCmd, Para):
        self.Cmd   = Cmd
        self.SlCmd = SlCmd
        self.Para  = Para

class Core ():
    def __init__ (self, apiSpecXml):
        self.PyLibs  = self.InitPyLibs (apiSpecXml)
        self.ApiList   = {}
        self.ClassInfo = {}
        self.InitApiList ()
        
        self.CmdList = {}
        self.OpList  = {}
        self.InitCmd ()

        self.RunStack = []
        self.LocalValue = {}

    def InitApiList (self):
        for libName, pyLib in self.PyLibs.items ():
            curExcepts = pyLib.Exceptions
            for mdName, pyMoudle in pyLib.Modules.items ():
                for clsName, cls in pyMoudle.Classes.items ():
                    for apiName, api in cls.Apis.items ():
                        absPath = libName + '.' + mdName + '.' + clsName + '.' + apiName
                        apiInfo = ApiInfo (cls.clsInit, clsName, api, curExcepts)
                        self.ApiList[absPath] = apiInfo
                    self.ClassInfo [clsName] = cls

                for apiName, api in pyMoudle.Apis.items ():
                    absPath = libName + '.' + mdName + '.' + apiName
                    self.ApiList[absPath] = ApiInfo (None, None, api, curExcepts)
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


    def InitCmd (self):
        self.CmdList['OO']  = SLCmd ('NewOO ()', 'cmd_newoo', SLCmd.Level1)
        self.CmdList['PO']  = SLCmd ('NewPO ()', 'cmd_newpo', SLCmd.Level1)
        self.CmdList['Inherit'] = SLCmd ('PyInherit ()', 'cmd_inherit', SLCmd.Level1)
        
        self.CmdList['For'] = SLCmd ('PyFor ()', 'cmd_for', SLCmd.Level2)
        

    def InitOp (self):
        self.OpList ['in'] = CmdOP ('in')


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
            raise Exception("No parameter in " + Cmd)
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
            
            ExeObj = eval (SlCmd.CmdName)      
            ExeObj.SetUp (ExeCode.ClsInit, ExeCode.Api, ExeCode.Exceps, ExeCode.Class)
            if hasattr (ExeObj, 'SetClass') == True:
                clsInfo = self.ClassInfo.get (ExeCode.Class)
                if clsInfo == None:
                    raise Exception(ExeCode.Class + " has no attributes")
                ExeObj.SetClass (clsInfo)
            
        return ExeObj.GenApp ()

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
        print (App)
        self.Write (App, OutPut)

