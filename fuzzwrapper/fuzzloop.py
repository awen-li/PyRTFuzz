
import os
import sys
import psutil
import signal
import time
from fuzzwrap import *
from multiprocessing import Process
from datetime import datetime
import shutil

LOG_DIR = 'fuzzlog/'
if not os.path.exists (LOG_DIR):
    os.mkdir (LOG_DIR, mode=0o777)
LogFile = LOG_DIR + 'pyfuzz.log'
if os.path.exists (LogFile):
    os.remove (LogFile)

def _Log (Msg=None):
    
    try:
        with open(LogFile, 'a') as LogF:
            CurTime = str(datetime.now())

            if Msg == None:
                LastApp = ''
                with open('CURRENT-level-fuzzing.log', 'r') as LF:
                    LastApp = LF.readline()
                print (f"[{CurTime}]\t{LastApp}", file=LogF)
            else:
                print (f"[{CurTime}]\t{Msg}", file=LogF)
    except:
        pass

def Clear ():
    KeyList = ['slow-unit-', 'crash-', 'Python', 'seeds', 'fuzzlog', 'apispec', 'clear', 'buildCPython', 'autorun', 'setPyEnv', 'PRTFuzz_perf', 'History']
    def IsInKeyList (name):
        NameLen = len (name)
        for key in KeyList:
            KeyLen = len (key)
            if KeyLen > NameLen:
                continue 
            if name[0:KeyLen] == key:
                return True
        return False
    
    absPath  = os.path.abspath ('.')
    if absPath.find ('/experiments') != -1:
        FileList = os.listdir (".")
        for file in FileList:
            if IsInKeyList (file) == True:
                continue       
            try:
                if os.path.isfile (file) == True:
                    os.remove (file)
                else:
                    shutil.rmtree(file, ignore_errors=True)
            except:
                pass
    
    DstDir = ['/', '/root']
    for dir in DstDir:
        FileList = os.listdir (dir)
        for file in FileList:
            try:
                if file in ['.dockerenv', '.bash_history', '.bashrc', '.condarc', '.profile', 
                            '.python_history', '.viminfo', '.wget-hsts', '.gitconfig']:
                    continue

                P = os.path.join (dir, file)
                if os.path.islink (P) == True or os.path.isdir (P) == True:
                    continue

                if os.path.isfile (P) == True:
                    os.remove (P)
            except:
                pass

def SysArg (Key):
    for arg in sys.argv:
        if arg.find (Key) != -1:
            return True
    return False

def BindCpu ():
    newArgv = []
    Cpu = None
    for arg in sys.argv:
        if arg.find ('-cpu=') != -1:
            Cpu = arg[arg.find('=')+1:]
        else:
            newArgv.append (arg)
    
    if Cpu != None:
        sys.argv = newArgv
        _Log (f"### bindding to CPU: {Cpu}")
    return Cpu

def Maskexcp ():
    newArgv = []
    Mask = False
    for arg in sys.argv:
        if arg.find ('-maskexcp') != -1:
            Mask = True
        else:
            newArgv.append (arg)

    if Mask == True:
        sys.argv = newArgv
        os.environ ['PYRTF_BYPASS_EXCEPTION'] = 'True'
        _Log ("### set PYRTF_BYPASS_EXCEPTION True!")
    return

def ProbPy ():
    newArgv = []
    ProbAll = True
    for arg in sys.argv:
        if arg.find ('-nopy') != -1:
            ProbAll = False
        else:
            newArgv.append (arg)

    if ProbAll == False:
        sys.argv = newArgv
        _Log (f"### No instrument for Python code")
    return ProbAll

def DTyped ():
    newArgv = []
    Untyped = False
    Typed = False
    for arg in sys.argv:
        if arg.find ('-typed') != -1:
            Typed = True
        elif arg.find ('-untyped') != -1:
            Untyped = True
        else:
            newArgv.append (arg)

    if Untyped == True or Typed == True:
        # in typed/untyped mode, open maskexcp
        os.environ ['PYRTF_BYPASS_EXCEPTION'] = 'True'
        _Log ("### set PYRTF_BYPASS_EXCEPTION True!")

        sys.argv = newArgv
    
    if Untyped == True:
        os.environ ['PYRTF_UNTYPED'] = 'True'
        _Log ("### set PYRTF_UNTYPED True!")

        
    return

if __name__ == '__main__':
    if SysArg ('clear'):
        Clear ()
        print ("### clear the directory done!")
        exit (0)
    
    Maskexcp ()
    DTyped ()
    CpuId = BindCpu ()
    ProbAll = ProbPy ()
    
    try:
        _Log ("### FuzzLoop: " + str(sys.argv))
        IterNum = 0
        while True:
            Fuzzer = Process(target=FuzzEntry, args=(CpuId,ProbAll,))
            Fuzzer.start()
            print ("\n### [%d]Fuzzer process starts [%d]\n" %(IterNum, Fuzzer.pid))

            time.sleep(15)
            CurProc = psutil.Process(Fuzzer.pid)
            ChildProc = CurProc.children(recursive=True)

            Fuzzer.join ()
            print ("\n\n### [%d]Fuzzer process exit [%d]\n" %(IterNum, Fuzzer.pid))
            IterNum += 1
            _Log ()
            Clear ()

            try:
                for proc in ChildProc:
                    if psutil.Process(proc.pid) != None:
                        os.kill(proc.pid, signal.SIGTERM)
            except:
                pass

    except Exception as e:
        print ("### fuzzloop exception: " + str(e))
    finally:
        Clear ()
        print ("### fuzzloop exit.....")


 
