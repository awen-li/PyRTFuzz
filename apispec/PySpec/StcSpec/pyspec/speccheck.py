
import os
import numpy as np
from .apispec_load import *

logFileName = "unrecognized_api_spec.txt"

class ApiSpecCheck ():
    def __init__ (self, ApiSpec='apispec.xml'):
        self.PyLibs = self.InitPyLibs (ApiSpec)
        if os.path.exists (logFileName):
            os.remove (logFileName)
        self.Types = {}

    def InitPyLibs (self, apiSpecXml):
        apiSpec = ApiSpecLoader (apiSpecXml)
        apiSpec.Parser ()
        return apiSpec.PyLibs

    def UpdateType (self, Type):
        num = self.Types.get (Type)
        if num == None:
            self.Types [Type] = 1
        else:
            self.Types [Type] = num + 1
        
    def CheckTypes (self, Api):
        for arg in Api.Args:
            type = arg.split (':')[1]
            if type == 'None':
                continue
            self.UpdateType (type)
            
        for arg in Api.PosArgs:
            type = arg.split (':')[1]
            if type == 'None':
                continue
            self.UpdateType (type)
    
        for arg in Api.KwoArgs:
            type = arg.split (':')[1]
            if type == 'None':
                continue
            self.UpdateType (type)     

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

    def LogTypeInfo (self):
        SortedTypes = sorted (self.Types.items (), key=lambda x:x[1], reverse=True)

        print ("\n\n")
        print ("##############       Type statistic     ####################\n")
        Index = 1
        for TypeName, Type in SortedTypes:
            print ("[%-4d] Type: %-32s, Number: %-8s" %(Index, TypeName, Type))
            Index += 1
        print ("############################################################\n")
            
        
    def Check (self):
        TotalApiNum = 0
        TypeKnowns   = 0
        for libName, pyLib in self.PyLibs.items ():
            for mdName, pyMoudle in pyLib.Modules.items ():
                for clsName, cls in pyMoudle.Classes.items ():
                    TotalApiNum += len (cls.Apis)
                    for apiName, api in cls.Apis.items ():
                        self.CheckTypes (api)
                        Typed = self.CheckApi (api)
                        if Typed == True:
                            TypeKnowns += 1
                        else:
                            self.LogApiInfo (libName, mdName, clsName, api)

                TotalApiNum += len (pyMoudle.Apis)
                for apiName, api in pyMoudle.Apis.items ():
                    self.CheckTypes (api)
                    Typed = self.CheckApi (api)
                    if Typed == True:
                        TypeKnowns += 1
                    else:
                        self.LogApiInfo (libName, mdName, '-', api)
                            
        print ("\n#####################   ApiSpecCheck   #####################")
        print ("### TotalApiNum   = %d" %TotalApiNum)
        print ("### TypeKnownsNum = %d" %TypeKnowns)
        print ("### Percentage    = %f" %(TypeKnowns/TotalApiNum*1.0))
        print ("############################################################\n")
    
        self.LogTypeInfo ()
                
