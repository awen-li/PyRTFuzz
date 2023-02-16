import os
import numpy as np
from .apispec_load import *
from .apispec_gen import *

class ApiExpr ():
    def __init__ (self, apiSpecXml='apispec.xml'):
        self.PyLibs = self.InitPyLibs (apiSpecXml)

    def InitPyLibs (self, apiSpecXml):
        apiSpec = ApiSpecLoader (apiSpecXml)
        apiSpec.Parser ()
        return apiSpec.PyLibs

    def SavePyLibs (self, path='expr-apispec.xml'):
        pyLibs = []
        for _, lib in self.PyLibs.items ():
            pyLibs.append (lib)
        
        ApiSpecGen.WriteXml (pyLibs, path)

    def DefValue (self, ValueStr, Type):
        if Type == 'str':
            return '\'' + ValueStr + '\''
        elif Type == 'int':
            return int(ValueStr)
        elif Type == 'NoneType':
            return str(None)
        elif Type == 'function':
            return ValueStr
        elif Type == 'bool':
            return bool (ValueStr)
        else:
            raise Exception("Unsupport type: " + str(Type))

    def GetExpr (self, Expr, Spec):
        #Spec.Show ()
        Expr += '('

        ArgNum = len (Spec.Args)
        #DefArgNum = len (Spec.Defas)
        ArgIndex = 0
        for arg in Spec.Args:
            para, ptype = arg.split(':')
            Expr += para
            #if DefArgNum >= ArgNum-ArgIndex:
            #    Expr += '=' + self.DefValue (Spec.Defas[DefArgNum-(ArgNum-ArgIndex)], ptype)

            ArgIndex += 1
            if ArgIndex < ArgNum:
                Expr += ','

        Expr += ')'          
        return Expr

    def GetApiExpr (self, ApiSpec, ApiPath, Obj=''):
        #print ("[API]" + ApiSpec.ApiName)
        ApiExpr = Obj
        if len (ApiSpec.Ret) != 0:
            ApiExpr += 'ret = '
        ApiExpr += ApiSpec.ApiName
        ApiExpr = self.GetExpr (ApiExpr, ApiSpec)
        #print (ApiExpr)
        return ApiExpr

    def GetClsInit (self, ClsSpec, InitSpec, ApiPath):
        #print ("[CLASS]" + ClsSpec.clsName)
        InitExpr = 'obj = ' + ClsSpec.clsName
        if InitSpec == None:
            InitExpr += '()'
        else:
            InitExpr = self.GetExpr (InitExpr, InitSpec)
        #print (InitExpr)
        return InitExpr     

    def GenExpr (self):
        ApiPath = ''
        for libName, pyLib in self.PyLibs.items ():
            if libName != '.':
                ApiPath = libName
            for mdName, pyMoudle in pyLib.Modules.items ():
                ApiPath += '.' + mdName
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