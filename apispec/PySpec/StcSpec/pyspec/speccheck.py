
import os
from .apispec_load import *

logFileName = "unrecognized_api_spec.txt"

class ApiSpecCheck ():
    def __init__ (self, ApiSpec='apispec.xml'):
        self.PyLibs = self.InitPyLibs (ApiSpec)
        if os.path.exists (logFileName):
            os.remove (logFileName)

    def InitPyLibs (self, apiSpecXml):
        apiSpec = ApiSpecLoader (apiSpecXml)
        apiSpec.Parser ()
        return apiSpec.PyLibs

    def CheckApi (self, Api):
        # args
        for arg in Api.Args:
            type = arg.split (':')[1]
            if type == 'None':
                return False

        for arg in Api.PosArgs:
            type = arg.split (':')[1]
            if type == 'None':
                return False

        for arg in Api.KwoArgs:
            type = arg.split (':')[1]
            if type == 'None':
                return False

        # return
        for r in Api.Ret:
            type = r.split (':')[1]
            if type == 'None':
                return False

        return True

    def LogApiInfo (self, libName, mdName, claName, api):
        with open (logFileName, "a") as f:
            print ("[lib]%s, [module]%s, [class]%s, [api]Args:%s, PosArgs:%s, KwoArgs:%s, Ret:%s"\
                %(libName, mdName, claName, str(api.Args), str(api.PosArgs), str(api.KwoArgs), str(api.Ret)), file=f)

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
                        else:
                            self.LogApiInfo (libName, mdName, clsName, api)

                TotalApiNum += len (pyMoudle.Apis)
                for apiName, api in pyMoudle.Apis.items ():
                    Typed = self.CheckApi (api)
                    if Typed == True:
                        TypeKnowns += 1
                    else:
                        self.LogApiInfo (libName, mdName, '-', api)
                            
        print ("\n#####################   ApiSpecCheck   #####################")
        print ("### TotalApiNum   = %d" %TotalApiNum)
        print ("### TypeKnownsNum = %d" %TypeKnowns)
        print ("### Percentage = %f" %(TypeKnowns/TotalApiNum*1.0))
        print ("############################################################\n")
    
    
                
