
import os
from .apispec_load import *

logFileName = "unrecognized_api_spec.txt"

class ApiSpecCheck ():
    def __init__ (self, ApiSpec='apispec.xml'):
        self.PyLibs = self.InitPyLibs (ApiSpec)
        if os.path.exists (logFileName):
            os.remove (logFileName)
        self.Types = {}
        self.Imports = []
        self.Excps = {}

    def InitPyLibs (self, apiSpecXml):
        apiSpec = ApiSpecLoader (apiSpecXml)
        apiSpec.Parser ()
        return apiSpec.PyLibs

    def GenInports (self, Target):
        Import = 'import ' + Target
        if IsExcept (Target):
            return
        if not Import in self.Imports:
            self.Imports.append (Import)

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
            print ("[lib]%s, [module]%s, [class]%s, [api]%s -- Args:%s, PosArgs:%s, KwoArgs:%s, Ret:%s"\
                %(libName, mdName, claName, api.ApiName, str(api.Args), str(api.PosArgs), str(api.KwoArgs), str(api.Ret)), file=f)

    def LogTypeInfo (self):
        SortedTypes = sorted (self.Types.items (), key=lambda x:x[1], reverse=True)
        TypeList = []

        print ("\n\n")
        print ("##############       Type statistic     ####################\n")
        Index = 1
        for TypeName, Type in SortedTypes:
            print ("[%-4d] Type: %-32s, Number: %-8s" %(Index, TypeName, Type))
            TypeList.append(TypeName)
            Index += 1
        print ("\n")
        print (TypeList)
        print ("############################################################\n")
            
    def LogImportInfo (self, logFileName='ImportList.txt'):
        if os.path.exists (logFileName):
            os.remove (logFileName)
        print ("Start LogImportInfo.")
        for Import in self.Imports:
            with open (logFileName, "a") as f:
                print (Import, file=f)

    def CheckExcp (self, PyExcpList):
        for pye in PyExcpList:
            exc = pye.exName
            Num = self.Excps.get (exc)
            if Num == None:
                self.Excps[exc] = 1
            else:
                self.Excps[exc] = Num + 1

    def LogExcps (self):
        Excps = dict(sorted(self.Excps.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))
        F = open ('ExcepList.txt', 'w')
        for exc, num in Excps.items ():
            print ("%-32s%-4d" %(exc, num), file=F)
        F.close ()

    def Check (self):
        TotalApiNum = 0
        TypeKnowns   = 0
        Modules = {}
        for libName, pyLib in self.PyLibs.items ():
            if libName != '.':
                self.GenInports (libName)
            for mdName, pyMoudle in pyLib.Modules.items ():
                self.GenInports (mdName)
                Modules[mdName.split ('.')[0]] = 1
                for clsName, cls in pyMoudle.Classes.items ():
                    #self.GenInports (mdName + '.' + clsName)
                    for apiName, api in cls.Apis.items ():
                        if apiName == '__init__':
                            continue

                        TotalApiNum += 1
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

                self.CheckExcp (pyMoudle.Exceptions)
                            
        print ("\n#####################   ApiSpecCheck   #####################")
        print ("### TotalApiNum   = %d" %TotalApiNum)
        print ("### TypeKnownsNum = %d" %TypeKnowns)
        print ("### Percentage    = %f" %(TypeKnowns/TotalApiNum*1.0))
        print ("############################################################\n")

        print ("### Modules = [%d]%s" %(len(Modules), str (list (Modules.keys ()))))
    
        self.LogTypeInfo ()
        self.LogImportInfo ()
        self.LogExcps ()
                
