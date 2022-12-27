
import os
import re
from .apispec import *
from .cmd_newoo import *
from .cmd_newpo import *
from .cmd_for import *

class ApiInfo ():
    def __init__ (self, ClsInit, Api, Exceps):
        self.ClsInit = ClsInit
        self.Api     = Api
        self.Exceps  = Exceps
            
class SLCmd ():
    def __init__ (self, CmdName, Module):
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
        self.ApiList = {}
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
                        self.ApiList[absPath] = ApiInfo (cls.clsInit, api, curExcepts)

                for apiName, api in pyMoudle.Apis.items ():
                    absPath = libName + '.' + mdName + '.' + apiName
                    self.ApiList[absPath] = ApiInfo (None, api, curExcepts)
                    
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
        apiSpec = ApiSpec (apiSpecXml)
        apiSpec.Parser ()
        return apiSpec.PyLibs

    def GetApiInfo (self, testApi):
        return self.ApiList.get (testApi)


    def InitCmd (self):
        self.CmdList['OO']  = SLCmd ('NewOO ()', 'cmd_newoo')
        self.CmdList['PO']  = SLCmd ('NewPO ()', 'cmd_newpo')
        self.CmdList['For'] = SLCmd ('PyFor ()', 'cmd_for')

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
        ExeObj = eval (SlCmd.CmdName)

        print (self.LocalValue)

        print ("@@@@ Exe -> " + exeCmd.Cmd + " to " + SlCmd.CmdName + " with " + exeCmd.Para)
        Value = self.GetVarValue (exeCmd.Para)
        print (Value)
        if Value != None:
            ExeCode = Value
            print ("run from local value: " + exeCmd.Para)
        else:  
            ExeCode = self.GetApiInfo (exeCmd.Para)
            ExeObj.SetUp (ExeCode.ClsInit, ExeCode.Api, ExeCode.Exceps)
            print ("run from original api: " + exeCmd.Para)
  
        return ExeObj.GenApp ()
  
    def Run (self, Script):    
        Script = Script.split ('\n')
        print (str(Script))
        
        for cmd in Script:
            cmd = cmd.strip ()
            if cmd == '':
                continue

            try:
                Var, exeCmd = self.Decode (cmd)
                Value = self.Exe (exeCmd)

                print ("Left Var = " + Var)
                if Var != None:
                    self.Push (Var, Value)
                
            except Exception as e:
                print ('Execution fail -> \"' + cmd + '\"')
                print (e)
                exit (0)
            
    


