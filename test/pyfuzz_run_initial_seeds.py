
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

InitFlag = '../experiments/seeds/initial_done'
if not os.path.exists (InitFlag):
    SrvPort = random.randint(10000, 65531)
    atheris.SetupPyFuzz('../apispec/PySpec/apispec.xml', SrvPort, ProbAll=False)
    atheris.GetInitialSeeds ('../experiments/seeds')
    atheris.Done ()

ModDir = os.walk('../experiments/seeds')
TotalNum = 0
SuccessNum = 0
for Path, Dirs, Pys in ModDir:      
    for py in Pys:
        Mod, Ext = os.path.splitext(py)
        if Ext != ".py":
            continue
        PyFile = os.path.join(Path, py)
        
        Cmd = 'python -m runone ' + PyFile
        sTimer = Timer(20, TimeOut)
        sTimer.start()
        
        print ("[%d]Execute: %s" %(TotalNum, Cmd), end='')
        RunProcess (Cmd)
        TotalNum += 1

        if RunResult == False:
            print (' ----> Fail')
        else:
            print (' ----> Success')
            SuccessNum += 1
        
        sTimer.cancel ()

print ("\n Success rate: [%d/%d]%.2f" %(SuccessNum, TotalNum, SuccessNum*1.0/TotalNum))








    
