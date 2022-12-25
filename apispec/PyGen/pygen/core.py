
import os
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


    def InitCmd (self):
        self.CmdList['NewOO'] = SLCmd ('NewOO ()', 'cmd_newoo')
        self.CmdList['NewPO'] = SLCmd ('NewPO ()', 'cmd_newpo')

    def InitOp (self):
        self.OpList ['in'] = CmdOP ('in')

    def Decode (self, stream):
        pass
        
    def GenApp (self, Script):
        for name, cmd in self.CmdList.items ():
            
            cmdExe = eval (cmd.CmdName)
            print (cmdExe)
            
    


