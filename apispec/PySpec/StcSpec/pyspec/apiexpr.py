import os
import numpy as np
from .apispec_load import *

class ApiExpr ():
    def __init__ (self, apiSpecXml='apispec.xml'):
        self.PyLibs = self.InitPyLibs (apiSpecXml)

    def InitPyLibs (self, apiSpecXml):
        apiSpec = ApiSpecLoader (apiSpecXml)
        apiSpec.Parser ()
        return apiSpec.PyLibs

    def GetApiExpr (self, ApiSpec, ApiPath):
        pass

    def DefValue (self, ValueStr, Type):
        if Type == 'str':
            return '\'' + ValueStr + '\''
        elif Type == 'int':
             return int(ValueStr)
        else:
            raise Exception("Unsupport type: " + str(Type))

    def GetClsInit (self, ClsSpec, InitSpec, ApiPath):
        print (ClsSpec.clsName + " -> " + str(ClsSpec.clsInit))
        InitExpr = 'obj = ' + ClsSpec.clsName + '('
        InitSpec.Show ()

        ArgNum = len (InitSpec.Args)
        DefArgNum = len (InitSpec.Defas)
        ArgIndex = 0
        for arg in InitSpec.Args:
            para, ptype = arg.split(':')
            InitExpr += para
            if DefArgNum >= ArgNum-ArgIndex:
                InitExpr += '=' + self.DefValue (InitSpec.Defas[DefArgNum-(ArgNum-ArgIndex)], ptype)

            ArgIndex += 1
            if ArgIndex < ArgNum:
                InitExpr += ','
            else:
                InitExpr += ')'
        print (InitExpr)
            

    def GenExpr (self):
        ApiPath = ''
        for libName, pyLib in self.PyLibs.items ():
            if libName != '.':
                ApiPath = libName
            for mdName, pyMoudle in pyLib.Modules.items ():
                ApiPath += '.' + mdName
                for clsName, cls in pyMoudle.Classes.items ():
                    for apiName, api in cls.Apis.items ():
                        if apiName == '__init__':
                            cls.clsInit = self.GetClsInit (cls, api, ApiPath)
                        else:
                            api.Expr = self.GetApiExpr (api, ApiPath)

                for apiName, api in pyMoudle.Apis.items ():
                    pass