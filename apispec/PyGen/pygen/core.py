
import os
from .apispec import *
from .cmd_newoo import *
from .cmd_newpo import *


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
                        OO = NewOO (cls.clsInit, api, curExcepts)
                        OO.GenApp ()

                        PO = NewPO (cls.clsInit, api, curExcepts)
                        PO.GenApp ()

                for apiName, api in pyMoudle.Apis.items ():
                    print ("### " + apiName)
                
                
        

class Core ():
    def __init__ (self, apiSpecXml)
        self.PyLibs = self.InitPyLibs (apiSpecXml)
        self.CmdList = None
        self.OpList  = None

    def InitPyLibs (self, apiSpecXml):
        apiSpec = ApiSpec (apiSpecXml)
        apiSpec.Parser ()
        return apiSpec.PyLibs


    def InitCmd (self):
        pass

    def InitOp (self):
        pass

    def Decode (self, stream):
        pass
        
    def GenApp (self, Script):
        pass
    


