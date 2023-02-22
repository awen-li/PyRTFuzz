import os
import random
import numpy as np
from .apispec_load import *
from .apispec_gen import *

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
        ApiExpr = Obj
        if len (ApiSpec.Ret) != 0:
            ApiExpr += 'ret = '
        ApiExpr += ApiSpec.ApiName
        ApiExpr, TypeList = self.GetExpr (ApiPath, ApiExpr, ApiSpec)
        #print (ApiExpr)
        return ApiExpr + '%%' + str(TypeList)

    def GetClsInit (self, ClsSpec, InitSpec, ApiPath):
        #print ("[CLASS]" + ClsSpec.clsName)
        InitExpr = 'obj = ' + ClsSpec.clsName
        if InitSpec == None:
            InitExpr += '()'
            TypeList  = []
        else:
            InitExpr, TypeList = self.GetExpr (ApiPath, InitExpr, InitSpec, SetDefault=True, Log=True)
        #print (InitExpr)
        return InitExpr + '%%' + str(TypeList)   

    def GenExpr (self):
        for libName, pyLib in self.PyLibs.items ():
            for mdName, pyMoudle in pyLib.Modules.items ():
                ApiPath = mdName
                for clsName, cls in pyMoudle.Classes.items ():
                    hasInit = False
                    for apiName, api in cls.Apis.items ():
                        if apiName == '__init__':
                            hasInit = True
                            cls.clsInit = self.GetClsInit (cls, api, ApiPath+'.'+clsName)
                        else:
                            api.Expr = self.GetApiExpr (api, ApiPath+'.'+clsName, 'obj.')
                    
                    if hasInit == False:
                        cls.clsInit = self.GetClsInit (cls, None, None)

                for apiName, api in pyMoudle.Apis.items ():
                    api.Expr = self.GetApiExpr (api, ApiPath)
        
        self.SavePyLibs ()