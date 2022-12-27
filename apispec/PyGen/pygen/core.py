
import os
import re
from .apispec import *
from .cmd_newoo import *
from .cmd_newpo import *
from .cmd_for import *


class AppGen ():
    def __init__ (self, apiSpecXml):
        apiSpec = ApiSpec (apiSpecXml)
        apiSpec.Parser ()
        self.PyLibs = apiSpec.PyLibs

        

    def Gen (self):
        for libName, pyLib in self.PyLibs.items ():
            print ("# " + libName)
            curExcepts = pyLib.Exceptions
            for mdName, pyMoudle in pyLib.Modules.items ():
                print ("## " + mdName)
                for clsName, cls in pyMoudle.Classes.items ():
                    print ("### " + clsName + ": " + cls.clsInit)
                    for apiName, api in cls.Apis.items ():
                        print ("#### " + apiName + " ---> " + api.Expr)
                        OO = NewOO ()
                        OO.SetUp (cls.clsInit, api, curExcepts)
                        OO.GenApp ()

                        PO = NewPO ()
                        PO.SetUp (cls.clsInit, api, curExcepts)
                        PO.GenApp ()

                        FOR = PyFor ()
                        FOR.SetUp (cls.clsInit, api, curExcepts)
                        FOR.GenApp ()

                for apiName, api in pyMoudle.Apis.items ():
                    print ("### " + apiName)
                
            
class SLCmd ():
    def __init__ (self, CmdName, Module):
        self.CmdName = CmdName
        self.Module  = Module

class CmdOP ():
    def __init__ (self, OpName):
        self.OpName = OpName


class ExeCmd ():
    def __init__ (self, SlCmd, Para):
        self.SlCmd = SlCmd
        self.Para  = Para

class Core ():
    def __init__ (self, apiSpecXml):
        self.PyLibs = self.InitPyLibs (apiSpecXml)
        self.CmdList = {}
        self.OpList  = {}

        self.InitCmd ()

    def InitPyLibs (self, apiSpecXml):
        apiSpec = ApiSpec (apiSpecXml)
        apiSpec.Parser ()
        return apiSpec.PyLibs

    def GetApiInfo (self, testApi):
        pass


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

        Value = Stmt = None
        if len (val) == 1:
            Stmt = val [0].strip ()         
        else:
            Value = val [0].strip ()
            Stmt  = val [1].strip ()

        Cmd = self.DeCmd (Stmt)
        Para = self.DePara(Stmt)
        SlCmd = self.GetSlCmd(Cmd)
        if SlCmd == None:
            raise Exception("Not support current cmd -> " + Cmd)

        return Value, ExeCmd (SlCmd, Para)
        
    def Run (self, Script):
        RunStack = []
        LocalValue = {}
        Script = Script.split ('\n')
        DebugPrint (str(Script))
        for cmd in Script:
            cmd = cmd.strip ()
            if cmd == '':
                continue

            try:
                Value, exeCmd = self.Decode (cmd)
                print (Value)
                print (exeCmd)
            except Exception as e:
                print ('Execution fail -> \"' + cmd + '\"')
                exit (0)
            
    


