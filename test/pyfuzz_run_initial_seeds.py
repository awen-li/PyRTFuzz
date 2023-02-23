
import os
import sys
import random
import atheris
import signal
import subprocess
from threading import Timer

SubProc = None
RunResult = 'False'
ErrorTypes = {}

def TimeOut ():
    if SubProc != None:
        os.kill(SubProc.pid, signal.SIGTERM)
        os.kill(SubProc.pid+1, signal.SIGTERM)
    global RunResult
    RunResult = 'TimeOut'
    LogError (RunResult)
    
def LogError (Err):
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
    
    if len (sys.argv) == 1:
        if RunResult != 'True':
            print ("[%d]Execute: %s ----> Fail (%d/%2.1f%%)" %(TotalNum, Cmd, SuccessNum, SuccessNum*100.0/TotalNum))
        else:
            print ("[%d]Execute: %s ----> Success (%d/%2.1f%%)" %(TotalNum, Cmd, SuccessNum, SuccessNum*100.0/TotalNum))
    else:
        Filter = sys.argv[1]
        if RunResult == Filter:
            print ("[%d]Execute: %s ----> Result: %s" %(TotalNum, Cmd, RunResult))
    return SuccessNum

def RunProcess (Cmd):
    global SubProc
    global RunResult

    SubProc = subprocess.Popen(Cmd, shell=True, stdout=subprocess.PIPE, stderr = subprocess.STDOUT)

    Ret = None
    while True:
        try:
            Line = SubProc.stdout.readline()
        except:
            print ("Except happened.......")
        
        if not Line: break
        Ret = Line.decode("utf-8").replace ("\n", "")
    
    if Ret == None:
        return
    
    if Ret != 'True':       
        RunResult = Ret
        LogError (Ret)
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

InitFlag = '../experiments/seeds/initial_done'
if not os.path.exists (InitFlag):
    SrvPort = random.randint(10000, 65531)
    atheris.SetupPyFuzz('../apispec/PySpec/apispec.xml', SrvPort, ProbAll=False)
    atheris.GetInitialSeeds ('../experiments/seeds')
    atheris.Done ()

AllTests = GetTests ('../experiments/seeds')
TotalNum = 0
SuccessNum = 0
for PyFile in AllTests:
    Cmd = 'python -m runone ' + PyFile
    sTimer = Timer(20, TimeOut)
    sTimer.start()
 
    RunProcess (Cmd)
    TotalNum += 1
    sTimer.cancel ()

    SuccessNum = FilterOut (Cmd, RunResult, SuccessNum, TotalNum)

print ("\n###Done, Success rate: %2.1f%%[%d/%d]" %(SuccessNum*100.0/TotalNum, SuccessNum, TotalNum))
ShowError ()

sys.exit (0)









    
