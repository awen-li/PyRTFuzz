
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
        Md = self.CurLib.Modules.get (MdName)
        if Md == None:
            return self.Tracing

        if Event == 'call':    
            ApiSpec = Md.Apis.get (Code.co_name)
            if ApiSpec != None:
                for arg in ApiSpec.Args:
                    para = arg.split(':')[0]
                    paraVal  = self.GetValue (Frame, para)
                    paraType = re.findall (r'<class \'(.+?)\'>', str(type(paraVal)))[0]
                    print (para + ' with type: ' + paraType)
        else:
            Msg = "[Python]:" + ScriptName + ": " +  str(LineNo) + " : " + Code.co_name + " -> EVENT = " + Event
            print (Msg)
        
        return self.Tracing

