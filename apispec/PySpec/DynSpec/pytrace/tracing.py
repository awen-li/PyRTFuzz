
import os
import re
import sys
import ast
from ast import *
import inspect
from multiprocessing import  Process
from pyspec import *

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
    def __init__(self, ApiSpecXml):
        self.ApiSpecXml = ApiSpecXml
        
        self.PyLibs = self.InitPyLibs (ApiSpecXml)
        self.CurLib = None

        self.Debug = False
        if os.environ.get ("PYDEBUG") != None:
            self.Debug = True

        self.PyLibPath = os.getenv ("PYTHON_LIBRARY")
        if self.PyLibPath == None:
            raise Exception("Please set PYTHON_LIBRARY first!")
        self.PyLibPathLen = len (self.PyLibPath)

        self.Passes = ["unittest", "importlib._bootstrap", 'pytrace']

    def __enter__(self):
        print ("[Tracing]----> __enter__................")
        _settrace(self.StartTracing)
        return self

    def __exit__(self, *_):
        _unsettrace()
        self.SavePyLibs ()
        print ("[Tracing]----> __exit__................")   

    def InitPyLibs (self, apiSpecXml):
        apiSpec = ApiSpecLoader (apiSpecXml)
        apiSpec.Parser ()
        return apiSpec.PyLibs

    def SavePyLibs (self):
        pyLibs = []
        for _, lib in self.PyLibs.items ():
            pyLibs.append (lib)
        
        ApiSpecGen.WriteXml (pyLibs, self.ApiSpecXml)

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

    
    def UpdateArgs (self, Frame, ArgsList):
        NewArgs = []
        hasNew  = False
        for arg in ArgsList:
            para, ptype = arg.split(':')
            if ptype == 'None':
                hasNew = True
                pval = self.GetValue (Frame, para)
                ptype = type(pval).__name__
            NewArgs.append (para + ':' + ptype)
        return hasNew, NewArgs

    def UpdateApiArgs (self, Frame, ApiSpec, LibName, MdName):
        # normal args
        if len (ApiSpec.Args) != 0:
            hasNew, NewArgs = self.UpdateArgs (Frame, ApiSpec.Args)
            ApiSpec.Args = NewArgs
            if hasNew == True:
                print ("###UpdateArgs " + MdName + "." + ApiSpec.ApiName + " arguments: " + str(NewArgs))

        # pos args
        if len (ApiSpec.PosArgs) != 0:
            hasNew, NewArgs = self.UpdateArgs (Frame, ApiSpec.PosArgs)
            ApiSpec.PosArgs = NewArgs
            if hasNew == True:
                print ("###UpdatePosArgs " + MdName + "." + ApiSpec.ApiName + " arguments: " + str(NewArgs))

        # kwo args
        if len (ApiSpec.KwoArgs) != 0:
            hasNew, NewArgs = self.UpdateArgs (Frame, ApiSpec.KwoArgs)
            ApiSpec.KwoArgs = NewArgs
            if hasNew == True:
                print ("###UpdateKwoArgs " + MdName + "." + ApiSpec.ApiName + " arguments: " + str(NewArgs))

    def UpdateApiRets (self, Frame, ApiSpec, LibName, MdName):
        NewRet = []
        for r in ApiSpec.Ret:
            ret, rtype = r.split(':')
            if rtype == 'None':
                rval = self.GetValue (Frame, ret)
                rtype = type(rval).__name__
                NewRet.append (ret + ':' + rtype)
                    
        ApiSpec.Ret = NewRet
        print ("###Update " + MdName + "." + ApiSpec.ApiName + " returns: " + str(NewRet))

    def GetApiSpec (self, Frame, CurMd, ApiName):
        sf = self.GetValue (Frame, 'self')
        if sf != None:
            clsname = sf.__class__.__name__
            if clsname.find ('EventCollector') != -1:
                for clsname, cls in CurMd.Classes.items ():
                    clsobj = self.GetValue (Frame, clsname)
                    if clsobj == None:
                        continue

                    apispec = cls.Apis.get (ApiName)
                    if apispec != None:
                        if self.Debug:
                            print ("[GetApiSpec-1][EventCollector]clsname = " + clsname + " and ApiName " + ApiName)
                        return apispec
                return None
            else:
                cls = CurMd.Classes.get (clsname)
                if self.Debug:
                    print ("[GetApiSpec-2]clsname = " + clsname + " and cls = " + str (cls) + ' with type = ' + str (type(sf)))
                
                if cls != None:
                    return cls.Apis.get (ApiName)
        else:
            # try class name
            cls = CurMd.Classes.get (ApiName)
            if cls != None:
                if self.Debug:
                    print ("[GetApiSpec-3]clsname~apiname = " + ApiName)
                return cls.Apis.get ('__init__')
            else:
                return CurMd.Apis.get (ApiName)

    def GetLibFile(self, CoFileName):
        if self.PyLibPath == None:
            raise Exception("Please set PYTHON_LIBRARY first!")
       
        if self.PyLibPath == '.':
            return CoFileName

        if self.PyLibPath != CoFileName [0:self.PyLibPathLen]:
            #print (self.PyLibPath + " <----> " + CoFileName)
            return None

        LibFile = CoFileName [self.PyLibPathLen:]
        if LibFile[0] == '/':
            LibFile = LibFile[1:]
        return LibFile

    def GetLibName (self, LibFileName):
        if self.PyLibPath == '.':
            return '.'
            
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
            return LibName + '.' + MdName
                
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

    def FilterOut (self, FileName):
        for file in self.Passes:
            if FileName.find (file) != -1:
                return True
        return False

    def ShowFrame (self, Frame):
        if not self.Debug:
            return
        
        print ("\n============== ShowFrame =====================")

        Index = 0
        for key, value in Frame.f_locals.items ():
            print (str(Index) + '-' + key, end=' -- ')
            print (value)
            Index += 1

        Index = 0
        for key, value in Frame.f_globals.items ():
            print (str(Index) + '-' + key, end=' -- ')
            print (value)
            Index += 1

        print ("================================================\n")

        
    def StartTracing (self, Frame, Event, Arg):
   
        Code = Frame.f_code
        self.CoName = Code.co_name

        if Event != 'call' and Event != 'return':
            return self.StartTracing

        if self.FilterOut(Code.co_filename) == True:
            return self.StartTracing

        LibFileName = self.GetLibFile (Code.co_filename)
        if LibFileName == None:
            return self.StartTracing

        LibName = self.GetLibName(LibFileName)
        MdName = self.GetMdName (LibName, LibFileName)

        if self.Debug:
            print ("LibName = " + LibName + " -> ModuleName = " + MdName + ": " + Code.co_name + ": " + Event)
        if MdName[0:1] == '_':
            return self.StartTracing
        
        Md = self.GetModule (LibName, MdName)
        if Md == None:
            return self.StartTracing

        if self.Debug:
            print ("[GetModule]" + Code.co_name + ' => ' + Event)
            
        FuncName = Code.co_name
        if FuncName [0:1] == '_':
            return self.StartTracing

        if Event == 'call':
            ApiSpec = self.GetApiSpec (Frame, Md, FuncName)
            if self.Debug:
                print ("[GetApiSpec]get  " + FuncName + " ApiSpec = " + str (ApiSpec))
            if  ApiSpec != None:
                self.UpdateApiArgs (Frame, ApiSpec, LibName, MdName)
                                
        elif Event == 'return':
            ApiSpec = self.GetApiSpec (Frame, Md, FuncName)
            if ApiSpec != None and len (ApiSpec.Ret) > 0:
                self.UpdateApiRets (Frame, ApiSpec, LibName, MdName)
        else:
            pass
        
        return self.StartTracing


class Task(Process):
    def __init__(self, Entry,     ApiSpecXml):
        super(Task, self).__init__()
        self.Entry  = Entry
        self.ApiSpecXml = ApiSpecXml
 
    def DynTrace (self, Entry, ApiSpecXml):
        fIndex = Entry.rfind ('/')
        if fIndex != -1:
            Path = Entry [0:fIndex]
            Entry = Entry [fIndex+1:]
            os.chdir (Path)

        try:
            print ("### Trace start -> " + os.getcwd () + ": " + Entry)   
            with open(Entry) as fp:
                code = compile(fp.read(), Entry, 'exec')

            globs = {
                '__file__': Entry,
                '__name__': '__main__',
                '__package__': None,
                '__cached__': None,
            }

            sys.argv = [Entry]
            with Tracing (ApiSpecXml) as T:
                exec(code, globs, globs)
  
        except OSError as oserr:
            sys.exit("Cannot run file %s because: %s" % (Entry, oserr))

        except SystemExit as sysrr:
            pass
            
            
    def run(self):
        print ("start run task")
        self.DynTrace (self.Entry, self.ApiSpecXml)

class IterTracing (Process):
    def __init__ (self, ApiSpecXml='apispec.xml'):
        super(IterTracing, self).__init__()
        self.ApiSpecXml = ApiSpecXml
        self.Except = ['multiprocessing', 'async']
        self.TestNum = 0

    def IsExcept (self, Entry):
        for e in self.Except:
            if Entry.find (e) != -1:
                return True
        return False

    def TracingTask (self, PyFile,      Index=0):
        print ("###[%d/%d]Start tacing %s" %(Index, self.TestNum, PyFile))
        trcTask = Task (PyFile, self.ApiSpecXml)
        trcTask.start()
        trcTask.join()
        

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
        

    def GetTestNum (self, CodeDir):
        return self.VisitTests (CodeDir)
        
        
    def StartTracing (self, CodeDir):
        self.TestNum = self.GetTestNum (CodeDir)
        self.VisitTests (CodeDir, self.TracingTask)
        

    def StartTracingSingle (self, Entry):
        self.TestNum = 1
        self.TracingTask (Entry)


        
