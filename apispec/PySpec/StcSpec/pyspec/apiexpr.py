import os
import subprocess
import random
from progressbar import ProgressBar
from .apispec_load import *
from .apispec_gen import *
from .utils import RunCmd, WriteValidate, OsExcepts
from .validate import Path2Imports, ValidatedApiList, Class2Bases


class ApiExpr ():
    def __init__ (self, apiSpecXml='apispec.xml'):
        self.PyLibs = self.InitPyLibs (apiSpecXml)
        self.ExprExcept = 'unrecognized-class-constructor.txt'
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
        WholePath = ApiPath
        if ApiSpec != None:
            WholePath += '.' + ApiSpec.ApiName

        if WholePath in ValidatedApiList:
            return True
        
        MdPos = WholePath.find ('.')
        ValidateCmd = f'python -c \'import {Imports}; print ({WholePath})\''
        Vres = RunCmd (ValidateCmd)
        if Vres.find ('Error: ') != -1:
            print ("Validate %s Fail. with Error: %s" %(WholePath, Vres))
            return False
        else:
            ValidatedApiList.append (WholePath)
            return True
        
    def GetModule (self, Module):
        for libName, pyLib in self.PyLibs.items ():
            for mdName, pyMoudle in pyLib.Modules.items ():
                if mdName != Module:
                    continue
                return pyMoudle
        return None
        
    def FastValidateExc (self, pyMoudle):
        Exceptions = pyMoudle.Exceptions
        ExceptsList = [exc.exName for exc in Exceptions]
        
        for impt in pyMoudle.Imports:
            ImptName = impt
            if ImptName.find(':') != -1:
                ImptName = ImptName.split(':')[0]
            if ImptName == pyMoudle.Name:
                continue
            ImptMd = self.GetModule (ImptName)
            if ImptMd == None:
                continue

            MdExcepts = ImptMd.Exceptions
            Prefix = len (ImptName)
            for excp in MdExcepts:
                if excp.exName[0:Prefix]== ImptName:
                    #print ('success ==> ' + excp.exName + ' ----- ' + ImptName)
                    ExceptsList.append (excp.exName)

        ExceptsList = list (set (ExceptsList + OsExcepts))

        Exceptions = [PyExcep(exc) for exc in ExceptsList]
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

    def GetClsInit (self, ClsSpec, InitSpec, ApiPath, IsFromBase=False):
        #print ("[CLASS]" + ClsSpec.clsName)
        InitExpr = 'obj = ' + ApiPath
        if InitSpec == None:
            InitExpr += '()'
            TypeList  = []
        else:
            InitExpr, TypeList = self.GetExpr (ApiPath, InitExpr, InitSpec, SetDefault=True, Log=(IsFromBase == False))
        #print (InitExpr)
        return InitExpr + '%%' + str(TypeList)
    
    def GetClassInit (self, cls):
        if cls == None:
            return None
        
        for apiName, api in cls.Apis.items ():
            if apiName == '__init__':
                return api
        return None

    def GetBaseClass (self, pyLib, Base):
        if Base == None:
            return None
        
        Index = Base.rfind ('.')
        Module = Base[0:Index]
        Class  = Base[Index+1:]
        if Module.find ('builtins') != -1:
            return None
        
        for libName, pyLib in self.PyLibs.items ():
            for mdName, pyMoudle in pyLib.Modules.items ():
                if mdName != Module:
                    continue
                for clsName, cls in pyMoudle.Classes.items ():
                    if clsName == Class:
                        return cls
        return None

    def GenExpr (self):
        print ("\n################ Fast Validating & generating API expr ################\n")
        FailNum = 0
        NoInitCls = 0
        par = ProgressBar ()
        for libName, pyLib in par(self.PyLibs.items ()):
            for mdName, pyMoudle in pyLib.Modules.items ():
                ApiPath = mdName
                MdApiNum = 0

                # validate imports
                Imports = self.GetImportList (ApiPath)
                ImportList = Imports.split (',')
                for Impt in ImportList:
                    if not Impt in pyMoudle.Imports:
                        pyMoudle.Imports.append (Impt)

                # validate CLASSes under the module
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
                    MdApiNum += len (NewApis)
                    
                    if hasInit == False:
                        BaseCls = self.GetBaseClass (pyLib, cls.Base)
                        InitSpec = self.GetClassInit (BaseCls)
                        cls.clsInit = self.GetClsInit (cls, InitSpec, ClsPath, IsFromBase=True)
                        #print ("### Update %s constructor as: %s" %(ClsPath, cls.clsInit))
                        NoInitCls += 1

                pyMoudle.Classes = NewClasses

                # validate APIs under the module
                NewApis = {}
                for apiName, api in pyMoudle.Apis.items ():
                    if not self.FastValidateApi (api, ApiPath, Imports):
                        FailNum += 1
                        continue
                    NewApis [apiName] = api
                    api.Expr = self.GetApiExpr (api, ApiPath)
                pyMoudle.Apis = NewApis
                MdApiNum += len (NewApis)

                # validate exceptions
                if MdApiNum != 0:
                    pyMoudle.Exceptions = self.FastValidateExc (pyMoudle)

        print ("### Total Validated with Failure = %d, Total %d classes with no init functions \r\n" %(FailNum, NoInitCls))
        self.SavePyLibs ()
        WriteValidate (Path2Imports, ValidatedApiList, Class2Bases)