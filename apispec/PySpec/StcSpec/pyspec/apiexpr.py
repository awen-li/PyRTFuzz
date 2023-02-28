import os
import subprocess
import random
from progressbar import ProgressBar
from .apispec_load import *
from .apispec_gen import *
from .utils import RunCmd
from .validate import Path2Imports, ValidatedApiList, Class2Bases


class ApiExpr ():
    def __init__ (self, apiSpecXml='apispec.xml'):
        self.PyLibs = self.InitPyLibs (apiSpecXml)
        self.ExprExcept = 'ExprExcept.txt'
        if os.path.exists (self.ExprExcept):
            os.remove (self.ExprExcept)

    def InitPyLibs (self, apiSpecXml):
        apiSpec = ApiSpecLoader (apiSpecXml)
        apiSpec.Parser ()
        return apiSpec.PyLibs

    def SavePyLibs (self, path='expr-apispec.xml'):
        pyLibs = []
        for _, lib in self.PyLibs.items ():
            pyLibs.append (lib)
        
        ApiSpecGen.WriteXml (pyLibs, path)

    def RandomStr (self, Length=32):
        Length = random.randint(0, Length)
        StrCtx = ''
        for i in range (0, Length):
            StrCtx += random.choice('1234567890QWERTYUIOPASDFGHJKLZXCVBNMabcdefghijklmnopqrstuvwxyz!@#$%^&*()')
        return StrCtx

    def DefValue (self, Type):
        if Type == 'str':
            return self.RandomStr ()
        elif Type == 'int':
            return random.randint(0, 65535)
        elif Type == 'bool':
            return ['True', 'False'][random.randint(0, 2)]
        elif Type == 'float':
            return random.uniform(0, 65535)
        elif Type == 'bytes':
            return bytes (self.RandomStr(), encoding='utf8')
        else:
            return 'None'

    def LogExprExcept (self, ApiPath, Expr):
        with open (self.ExprExcept, 'a') as log:
            print ("%s -- %s" %(ApiPath, Expr), file=log)

    def GetImportList (self, ApiPath):
        ImportList = Path2Imports.get (ApiPath)
        if ImportList != None:
            return ImportList

        ImportList = []
        MdSecs = ApiPath.split ('.')
        Md = ''
        for m in MdSecs:
            if Md == '':
                Md = m
            else:
                Md += '.' + m
            Cmd = f'python -c \'import {Md}; print ({Md}.__class__.__name__)\''
            #print ("\t ->Cmd: " + Cmd)
            Mtype = RunCmd (Cmd)
            if Mtype == 'module':
                ImportList.append (Md)
        ImportList = ','.join (ImportList)
        Path2Imports[ApiPath] = ImportList
        #print ("### ImportList = " + ImportList)
        return ImportList

    def FastValidateApi (self, ApiSpec, ApiPath, Imports):
        if ApiPath in ValidatedApiList:
            return True
        
        WholePath = ApiPath
        if ApiSpec != None:
            WholePath += '.' + ApiSpec.ApiName
        MdPos = WholePath.find ('.')
        ValidateCmd = f'python -c \'import {Imports}; print ({WholePath})\''
        Vres = RunCmd (ValidateCmd)
        if Vres.find ('Error: ') != -1:
            print ("Validate %s Fail. with Error: %s" %(WholePath, Vres))
            return False
        else:
            ValidatedApiList.append (ApiPath)
            return True
        
    def FastValidateExc (self, Exceptions):     
        return Exceptions

    def GetExpr (self, ApiPath, Expr, Spec, SetDefault=False, Log=False):
        #Spec.Show ()    
        ArgNum = len (Spec.Args)
        DefArgNum = len (Spec.Defas)
        if ArgNum != DefArgNum and Log == True:
            self.LogExprExcept (ApiPath, Expr)

        TypeList = []
        Expr += '('

        ArgIndex = 0
        for arg in Spec.Args:
            para, ptype = arg.split(':')
            if SetDefault == False:
                Expr += para

                ArgIndex += 1
                if ArgIndex < ArgNum:
                    Expr += ','
            else:
                if ArgIndex < (ArgNum-DefArgNum):
                    Expr += str(self.DefValue (ptype))

                    ArgIndex += 1
                    if ArgIndex < (ArgNum-DefArgNum):
                        Expr += ','
                else:
                    pass
            TypeList.append (ptype)

        Expr += ')'          
        return Expr, TypeList

    def GetApiExpr (self, ApiSpec, ApiPath, Obj=''):
        #print ("[API]" + ApiSpec.ApiName)
        ApiExpr = ''
        if len (ApiSpec.Ret) != 0:
            ApiExpr += 'ret = '
        
        if Obj == '':
            ApiExpr += ApiPath + '.'
        else:
            ApiExpr += Obj
        
        ApiExpr += ApiSpec.ApiName
        ApiExpr, TypeList = self.GetExpr (ApiPath, ApiExpr, ApiSpec)
        #print (ApiExpr)
        return ApiExpr + '%%' + str(TypeList)

    def GetClsInit (self, ClsSpec, InitSpec, ApiPath):
        #print ("[CLASS]" + ClsSpec.clsName)
        InitExpr = 'obj = ' + ApiPath
        if InitSpec == None:
            InitExpr += '()'
            TypeList  = []
        else:
            InitExpr, TypeList = self.GetExpr (ApiPath, InitExpr, InitSpec, SetDefault=True, Log=True)
        #print (InitExpr)
        return InitExpr + '%%' + str(TypeList)   

    def GenExpr (self):
        print ("\n################ Fast Validating & generating API expr ################\n")
        FailNum = 0
        par = ProgressBar ()
        for libName, pyLib in par(self.PyLibs.items ()):
            for mdName, pyMoudle in pyLib.Modules.items ():
                ApiPath = mdName

                Imports = self.GetImportList (ApiPath)
                ImportList = Imports.split (',')
                for Impt in ImportList:
                    if not Impt in pyMoudle.Imports:
                        pyMoudle.Imports.append (Impt)

                pyMoudle.Exceptions = self.FastValidateExc (pyMoudle.Exceptions)
                
                NewClasses = {}
                for clsName, cls in pyMoudle.Classes.items ():
                    
                    ClsPath = ApiPath+'.'+clsName
                    if not self.FastValidateApi (None, ClsPath, Imports):
                        FailNum += len (cls.Apis)
                        continue           
                    NewClasses [clsName] = cls

                    hasInit = False
                    NewApis = {}
                    for apiName, api in cls.Apis.items ():
                        if apiName == '__init__':
                            hasInit = True
                            cls.clsInit = self.GetClsInit (cls, api, ClsPath)
                        else:
                            if not self.FastValidateApi (api, ClsPath, Imports):
                                FailNum += 1
                                continue

                            api.Expr = self.GetApiExpr (api, ClsPath, 'obj.')
                        NewApis [apiName] = api
                    cls.Apis = NewApis
                    
                    if hasInit == False:
                        cls.clsInit = self.GetClsInit (cls, None, ClsPath)
                pyMoudle.Classes = NewClasses

                NewApis = {}
                for apiName, api in pyMoudle.Apis.items ():
                    if not self.FastValidateApi (api, ApiPath, Imports):
                        FailNum += 1
                        continue
                    NewApis [apiName] = api
                    api.Expr = self.GetApiExpr (api, ApiPath)
                pyMoudle.Apis = NewApis

        print ("### Total Validated with Failure = %d \r\n" %FailNum)
        self.SavePyLibs ()
        WriteValidate (Path2Imports, ValidatedApiList, Class2Bases)