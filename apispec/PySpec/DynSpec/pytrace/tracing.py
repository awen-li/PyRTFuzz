
import os
import re
import sys
import inspect
from pygen import *

try:
    import threading
except ImportError:
    _settrace = sys.settrace

    def _unsettrace():
        sys.settrace(None)
else:
    def _settrace(func):
        threading.settrace(func)
        sys.settrace(func)

    def _unsettrace():
        sys.settrace(None)
        threading.settrace(None)


class Tracing:
    def __init__(self, CurLib, ApiSpecXml='apispec.xml'):
        self.PyLibs = self.InitPyLibs (ApiSpecXml)
        self.CurLib = self.PyLibs.get (CurLib)
        if self.CurLib == None:
            raise Exception("Tracing: current lib" + CurLib + " not found!")

        self.SetUp = False
        if os.environ.get ("case_name") == None:
            self.IsSingleCase = False
        else:
            self.IsSingleCase = True

        self.Debug = False
        if os.environ.get ("pygen_debug") != None:
            self.Debug = True

    def __enter__(self):
        print ("----> __enter__................IsSingleCase->", self.IsSingleCase)
        _settrace(self.Tracing)
        return self

    def __exit__(self, *_):
        print ("----> __exit__................")
        _unsettrace()

    def InitPyLibs (self, apiSpecXml):
        apiSpec = ApiSpec (apiSpecXml)
        apiSpec.Parser ()
        return apiSpec.PyLibs

    def GetValue(self, Frame, ValName):
        if ValName in Frame.f_locals:
            return Frame.f_locals[ValName]
        elif ValName in Frame.f_globals:
            return Frame.f_globals[ValName]
        else:
            Builtins = Frame.f_globals['__builtins__']
            if isinstance(Builtins, dict) and (ValName in Builtins):
                return Builtins[ValName]
            elif isinstance(Builtins, Module) and hasattr(Builtins, ValName):
                return getattr(Frame.f_globals['__builtins__'], ValName)
        return None

    def UpdateApiArgs (self, Frame, ApiSpec):
        NewArgs = []
        hasNew  = False
        for arg in ApiSpec.Args:
            para, ptype = arg.split(':')
            if ptype == 'None':
                hasNew = True
                pval = self.GetValue (Frame, para)
                ptype = type(pval).__name__
            NewArgs.append (para + ':' + ptype)

        ApiSpec.Args = NewArgs
        if hasNew == True:
            print ("###Update " +  ApiSpec.ApiName + " arguments: " + str(NewArgs))

    def UpdateApiRets (self, Frame, ApiSpec):
        NewRet = []
        for r in ApiSpec.Ret:
            ret, rtype = r.split(':')
            if rtype == 'None':
                rval = self.GetValue (Frame, ret)
                rtype = type(rval).__name__
                NewRet.append (ret + ':' + rtype)
                    
        ApiSpec.Ret = NewRet
        print ("###Update " +  ApiSpec.ApiName + " returns: " + str(NewRet))

    def GetApiSpec (self, Frame, CurMd, ApiName):
        sf = self.GetValue (Frame, 'self')
        if sf != None:
            clsname = sf.__class__.__name__
            cls = CurMd.Classes.get (clsname)
            if cls != None:
                return cls.Apis.get (ApiName)
        else:
            return CurMd.Apis.get (ApiName)

    def GetModule (self, MdName):
        Md = self.CurLib.Modules.get (MdName)
        if Md != None:
            return Md

        for libName, lib in self.PyLibs.items ():
            if libName == self.CurLib.Name:
                continue

            Md = lib.Modules.get (MdName)
            if Md != None:
                self.CurLib = lib
                return Md
        
        return None
            
        
    def Tracing(self, Frame, Event, Arg):
        if self.IsSingleCase and self.SetUp == False:
            Step = os.environ.get ("case_step")
            if Step == "setup":
                self.SetUp = True
            else:
                return self.Tracing
        
        Code = Frame.f_code
        self.CoName = Code.co_name

        _, ScriptName = os.path.split(Code.co_filename)
        LineNo  = Frame.f_lineno

        MdName = ScriptName.split('.')[0]
        Md = self.GetModule (MdName)
        if Md == None:
            if MdName.find('test') == -1:
                print ("####GetModule fail -> " + MdName)
            return self.Tracing

        FuncName = Code.co_name
        if FuncName [0:1] == '_':
            return self.Tracing

        if Event == 'call':
            ApiSpec = self.GetApiSpec (Frame, Md, FuncName)
            if  ApiSpec != None:
                self.UpdateApiArgs (Frame, ApiSpec)
                                
        elif Event == 'return':
            ApiSpec = self.GetApiSpec (Frame, Md, FuncName)
            if ApiSpec != None and len (ApiSpec.Ret) > 0:
                self.UpdateApiRets (Frame, ApiSpec)
        else:
            Msg = "[Python]:" + ScriptName + ": " +  str(LineNo) + " : " + FuncName + " -> EVENT = " + Event
            #print (Msg)

        return self.Tracing

