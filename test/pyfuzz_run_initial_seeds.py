
import os
import sys
import random
import atheris
import signal
import subprocess
from threading import Timer

SubProc = None
RunResult = False

def TimeOut ():
    if SubProc != None:
        os.kill(SubProc.pid, signal.SIGTERM)
        os.kill(SubProc.pid+1, signal.SIGTERM)
    global RunResult
    RunResult = False
    

def RunProcess (Cmd):
    global SubProc
    global RunResult

    SubProc = subprocess.Popen(Cmd, shell=True, stdout=subprocess.PIPE, stderr = subprocess.STDOUT)

    while True:
        try:
            Line = SubProc.stdout.readline()
        except:
            print ("Except happened.......")
        if not Line: break
        Ret = Line.decode("utf-8").replace ("\n", "")
        if Ret != 'True':       
            RunResult = False
        else:
            RunResult = True
        break
    return

def GetTests (Path):
    AllTests = []
    ModDir = os.walk(Path)
    TotalNum = 0
    SuccessNum = 0
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
    if RunResult == False:
        print ("[%d]Execute: %s ----> Fail (%d/%.2f)" %(TotalNum, Cmd, SuccessNum, SuccessNum*1.0/TotalNum))
    else:
        SuccessNum += 1
        print ("[%d]Execute: %s ----> Success (%d/%.2f)" %(TotalNum, Cmd, SuccessNum, SuccessNum*1.0/TotalNum))       

print ("\n###Done, Success rate: [%d/%d]%.2f" %(SuccessNum, TotalNum, SuccessNum*1.0/TotalNum))
sys.exit (0)









    
