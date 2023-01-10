
import os
import sys
import inspect

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
    def __init__(self, ApiSpecXml='apispec.xml'):
        self.ApiSpecXml = ApiSpecXml

        self.TracedStmts = 0
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
        print ("----> __exit__................, TracedStmts = ", self.TracedStmts)
        _unsettrace()

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

        if Event == 'call':    
            Msg = "[Python]:" + ScriptName + ": " +  str(LineNo) + " : calling " + Code.co_name
            if Code.co_name == 'add':
                x = self.GetValue (Frame, 'x')
                print (type(x))

                y = self.GetValue (Frame, 'y')
                print (type(y))

            if Code.co_name == 'show':
                info = self.GetValue (Frame, 'info')
                print (type(info))
        else:
            Msg = "[Python]:" + ScriptName + ": " +  str(LineNo) + " : " + Code.co_name + " -> EVENT = " + Event
        print (Msg)
        
        return self.Tracing

