
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

        Msg = "[Python]:" + ScriptName + ": " +  str(LineNo) + " : " + Code.co_name
        print (Msg)
        
        return self.Tracing

