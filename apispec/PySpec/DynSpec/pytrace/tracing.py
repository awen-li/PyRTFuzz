
import os
import re
import sys
import inspect
from multiprocessing import  Process
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
    def __init__(self, PyLibs):
        self.PyLibs = PyLibs
        self.CurLib = None

        self.Debug = False
        if os.environ.get ("pygen_debug") != None:
            self.Debug = True

        self.PyLibPath = os.getenv ("PYTHON_LIBRARY")
        if self.PyLibPath == None:
            raise Exception("Please set PYTHON_LIBRARY first!")
        self.PyLibPathLen = len (self.PyLibPath)

    def __enter__(self):
        print ("[Tracing]----> __enter__................")
        _settrace(self.StartTracing)
        return self

    def __exit__(self, *_):
        print ("[Tracing]----> __exit__................")
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

    def UpdateApiArgs (self, Frame, ApiSpec, LibName, MdName):
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
            print ("###Update " +  LibName + "." + MdName + "." + ApiSpec.ApiName + " arguments: " + str(NewArgs))

    def UpdateApiRets (self, Frame, ApiSpec, LibName, MdName):
        NewRet = []
        for r in ApiSpec.Ret:
            ret, rtype = r.split(':')
            if rtype == 'None':
                rval = self.GetValue (Frame, ret)
                rtype = type(rval).__name__
                NewRet.append (ret + ':' + rtype)
                    
        ApiSpec.Ret = NewRet
        print ("###Update " +  LibName + "." + MdName + "." + ApiSpec.ApiName + " returns: " + str(NewRet))

    def GetApiSpec (self, Frame, CurMd, ApiName):
        sf = self.GetValue (Frame, 'self')
        if sf != None:
            clsname = sf.__class__.__name__
            cls = CurMd.Classes.get (clsname)
            if cls != None:
                return cls.Apis.get (ApiName)
        else:
            return CurMd.Apis.get (ApiName)

    def GetLibFile(self, CoFileName):
        if self.PyLibPath == None:
            raise Exception("Please set PYTHON_LIBRARY first!")

        if self.PyLibPath != CoFileName [0:self.PyLibPathLen]:
            #print (self.PyLibPath + " <----> " + CoFileName)
            return None

        LibFile = CoFileName [self.PyLibPathLen:]
        if LibFile[0] == '/':
            LibFile = LibFile[1:]
        return LibFile

    def GetLibName (self, LibFileName):
        Index = LibFileName.find ('/')
        if Index == -1:
            return '.'
        else:
            return LibFileName [0:Index]

    def GetMdName (self, LibName, LibFileName):
        LibFileName = LibFileName.split ('.')[0]
        if LibName == '.':
            return LibFileName
        else:
            MdName = LibFileName[len(LibName)+1:].replace ('/', '.')
            return MdName
                
    def GetModule (self, LibName, MdName):
        if self.CurLib != None:
            Md = self.CurLib.Modules.get (MdName)
            if Md != None:
                return Md

        self.CurLib = self.PyLibs.get (LibName)
        if self.CurLib == None:
            return None
            
        Md = self.CurLib.Modules.get (MdName)
        if Md != None:
            return Md
            
        return None
            
        
    def StartTracing (self, Frame, Event, Arg):
   
        Code = Frame.f_code
        self.CoName = Code.co_name

        # for debug
        #if Code.co_filename.find ("mail") == -1:
        #    return self.Tracing

        LibFileName = self.GetLibFile (Code.co_filename)
        if LibFileName == None:
            return self.StartTracing

        LibName = self.GetLibName(LibFileName)
        MdName = self.GetMdName (LibName, LibFileName)
        if MdName[0:1] == '_':
            return self.StartTracing
        
        Md = self.GetModule (LibName, MdName)
        if Md == None:
            #print ("####GetModule fail -> " + MdName)
            return self.StartTracing

        FuncName = Code.co_name
        if FuncName [0:1] == '_':
            return self.StartTracing

        if Event == 'call':
            ApiSpec = self.GetApiSpec (Frame, Md, FuncName)
            if  ApiSpec != None:
                self.UpdateApiArgs (Frame, ApiSpec, LibName, MdName)
                                
        elif Event == 'return':
            ApiSpec = self.GetApiSpec (Frame, Md, FuncName)
            if ApiSpec != None and len (ApiSpec.Ret) > 0:
                self.UpdateApiRets (Frame, ApiSpec, LibName, MdName)
        else:
            Msg = "[Python]:" + Code.co_filename + ": " +  str(Frame.f_lineno) + " : " + FuncName + " -> EVENT = " + Event
            #print (Msg)

        return self.StartTracing


class Task(Process):
    def __init__(self, Entry, PyLibs):
        super(Task, self).__init__()
        self.Entry  = Entry
        self.PyLibs = PyLibs

    def DynTrace (self, Entry, PyLibs):
        fIndex = Entry.rfind ('/')
        if fIndex != -1:
            Path = Entry [0:fIndex]
            Entry = Entry [fIndex+1:]
            os.chdir (Path)
            
        try:
            with open(Entry) as fp:
                code = compile(fp.read(), Entry, 'exec')

            globs = {
                '__file__': Entry,
                '__name__': '__main__',
                '__package__': None,
                '__cached__': None,
            }

            sys.argv = [Entry]
            with Tracing (PyLibs) as T:
                exec(code, globs, globs)
                self.PyLibs = T.PyLibs
                
        except OSError as oserr:
            sys.exit("Cannot run file %s because: %s" % (Entry, oserr))
        except SystemExit as sysrr:
            pass
            
    def run(self):
        print ("start run task")
        self.DynTrace (self.Entry, self.PyLibs)

class IterTracing (Process):
    def __init__ (self, ApiSpecXml='apispec.xml'):
        super(IterTracing, self).__init__()
        self.PyLibs = self.InitPyLibs (ApiSpecXml)
        self.Except = ['multiprocessing', 'async']
        self.TestNum = 0

    def IsExcept (self, Entry):
        for e in self.Except:
            if Entry.find (e) != -1:
                return True
        return False

    def InitPyLibs (self, apiSpecXml):
        apiSpec = ApiSpec (apiSpecXml)
        apiSpec.Parser ()
        return apiSpec.PyLibs

    def TracingTask (self, PyFile, Index=0):
        print ("###[%d/%d]Start tacing %s" %(Index, self.TestNum, PyFile))
        trcTask = Task (PyFile, self.PyLibs)
        trcTask.start()
        trcTask.join()
        self.PyLibs = trcTask.PyLibs
        

    def VisitTests (self, CodeDir, HandleHook=None):
        TestNum = 0
        TestWalk = os.walk(CodeDir)
        for Path, Dirs, Pys in TestWalk:
            for py in Pys:
                if not re.search (r'test.*.py$', py) or self.IsExcept (py) == True:
                    continue
                
                PyFile  = os.path.join(Path, py)
                if HandleHook != None:
                    HandleHook (PyFile, TestNum)
                
                TestNum += 1
        return TestNum
        
    def StartTracing (self, CodeDir):
        self.TestNum = self.VisitTests (CodeDir)
        self.VisitTests (CodeDir, self.TracingTask)
        

    def StartTracingSingle (self, Entry):
        self.TestNum = 1
        self.TracingTask (Entry)


        
