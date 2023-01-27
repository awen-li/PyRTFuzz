
import os
from .apispec_load import *

class ApiSpecCheck ():
    def __init__ (self, ApiSpec='apispec.xml'):
        self.PyLibs = self.InitPyLibs (ApiSpec)

    def InitPyLibs (self, apiSpecXml):
        apiSpec = ApiSpecLoader (apiSpecXml)
        apiSpec.Parser ()
        return apiSpec.PyLibs

    def CheckApi (self, Api):
        pass

    def Check (self):
        TotalApiNum = 0
        TypeKnowns   = 0
        for libName, pyLib in self.PyLibs.items ():
            curExcepts = pyLib.Exceptions
            for mdName, pyMoudle in pyLib.Modules.items ():
                for clsName, cls in pyMoudle.Classes.items ():
                    TotalApiNum += len (cls.Apis)
                    for apiName, api in cls.Apis.items ():
                        Typed = self.CheckApi (api)
                        if Typed == True:
                            TypeKnowns += 1

                TotalApiNum += len (pyMoudle.Apis)
                for apiName, api in pyMoudle.Apis.items ():
                    Typed = self.CheckApi (api)
                    if Typed == True:
                        TypeKnowns += 1
                            
        print ("\n#####################   ApiSpecCheck   #####################")
        print ("### TotalApiNum   = %d" %TotalApiNum)
        print ("### TypeKnownsNum = %d" %TypeKnowns)
        print ("### Percentage = %f" %(TypeKnowns/TotalApiNum*1.0))
        print ("############################################################\n")
    
    
                
