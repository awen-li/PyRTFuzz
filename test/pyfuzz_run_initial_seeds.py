
import os
import sys
import random
import signal
import psutil
import subprocess
from threading import Timer
from fuzzwrap import *
from platform import python_version

py_version = python_version()

SubProc = None
RunResult = 'False'
CurCase = ''
ErrorTypes = {}
RunDir = 'Temp'
ErrorLogDir = '../ErroLog/'

def KillAll (Pid):
    CurProc = psutil.Process(Pid)
    Children = CurProc.children(recursive=True)
    try:
        for ch in Children:
            os.kill(ch.pid, signal.SIGTERM)
        os.kill (Pid, signal.SIGTERM)
    except:
        pass

def TimeOut ():
    global RunResult
    global CurCase

    if SubProc != None:
        KillAll (SubProc.pid)
    
    RunResult = 'TimeOut'
    LogError (RunResult, CurCase)
    
def LogError (Err, Cmd):
    if not os.path.exists (ErrorLogDir):
        os.mkdir (ErrorLogDir)

    if len (Err) > 32:
        Err = 'Other'
    try:
        with open (ErrorLogDir + "error_rpt_" + Err + ".log", 'a') as F:
            print (Cmd, file=F)
    except:
        pass
    
    ErrNum = ErrorTypes.get (Err)
    if ErrNum == None:
        ErrorTypes[Err] = 1
    else:
        ErrorTypes[Err] = ErrNum+1

def ShowError ():
    print ("\n################## ERROR details ##################")
    for err, num in ErrorTypes.items ():
        print ("### Error Type: %-16s, Number:%-4d" %(err, num))
    print ("###################################################\n")

def FilterOut (Cmd, Ret, SuccessNum, TotalNum):
    if RunResult == 'True':
        SuccessNum += 1
    
    if RunResult != 'True':
        print ("[%d]Execute: %s ----> Fail (%d/%2.1f%%)" %(TotalNum, Cmd, SuccessNum, SuccessNum*100.0/TotalNum))
    else:
        print ("[%d]Execute: %s ----> Success (%d/%2.1f%%)" %(TotalNum, Cmd, SuccessNum, SuccessNum*100.0/TotalNum))
        
    return SuccessNum

def TransError (Err):
    if Err.find ('AttributeError: \'NoneType\'') != -1:
        return 'AttributeError_NoneType'
    elif Err.find ('TypeError: \'NoneType\'') != -1:
        return 'TypeError_NoneType'
    else:
        return False

def RunProcess (Cmd):
    global SubProc
    global RunResult
    global CurCase

    CurCase = Cmd

    SubProc = subprocess.Popen(Cmd, shell=True, stdout=subprocess.PIPE, stderr = subprocess.STDOUT)
    Ret = None
    while True:
        try:
            Line = SubProc.stdout.readline()
        except:
            print ("Except happened.......")
        
        if not Line: break
        Ret = Line.decode("utf-8").replace ("\n", "")
        Trans = TransError (Ret)
        if  Trans != False:
            Ret = Trans
            break
    
    if Ret == None:
        return
    
    if Ret != 'True':       
        RunResult = Ret
        LogError (Ret, Cmd)
    else:
        RunResult = 'True'
    return

def GetTests (Path):
    AllTests = []
    ModDir = os.walk(Path)
    for Path, Dirs, Pys in ModDir:      
        for py in Pys:
            Mod, Ext = os.path.splitext(py)
            if Ext != ".py":
                continue
            PyFile = os.path.join(Path, py)
            AllTests.append (PyFile)
    return AllTests

SeedDir = os.path.abspath (f'../experiments/seeds_python{py_version}')
InitFlag = SeedDir + '/initial_done'
if not os.path.exists (InitFlag):
    SrvPort = random.randint(10000, 65531)
    SetupPyFuzz('../apispec/PySpec/apispec.xml', SrvPort, ProbAll=False)
    GetInitialSeeds (SeedDir)
    Done ()

if len (sys.argv) == 1:
    if not os.path.exists (RunDir):
        os.mkdir (RunDir)
    os.chdir (RunDir)

    AllTests = GetTests (SeedDir)
    if len (AllTests) == 0:
        print ("### Get no APPs from %s" %SeedDir)
        exit (0)
    TotalNum = 0
    SuccessNum = 0
    for PyFile in AllTests:
        Cmd = 'python -m runone ' + PyFile
        sTimer = Timer(30, TimeOut)
        sTimer.start()
    
        RunProcess (Cmd)
        TotalNum += 1
        sTimer.cancel ()

        SuccessNum = FilterOut (Cmd, RunResult, SuccessNum, TotalNum)

    print ("\n###Done, Success rate: %2.1f%%[%d/%d]" %(SuccessNum*100.0/TotalNum, SuccessNum, TotalNum))
    ShowError ()
    sys.exit (0)
else:
    ErrLog = sys.argv[1]
    AllExe = []
    with open (ErrLog, 'r') as F:
        AllExe = F.readlines()
        for exe in AllExe:
            Cmd = exe.replace ('\n', '')
            print ("\n### Run " + Cmd)
            os.system (Cmd)











    
