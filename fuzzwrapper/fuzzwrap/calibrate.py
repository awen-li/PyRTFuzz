import os
import sys
import signal
import subprocess
import psutil
from subprocess import *
from multiprocessing import  Process
from progressbar import ProgressBar

class Task(Process):
    def __init__(self, TaskId, SeedList):
        super(Task, self).__init__()
        self.TaskId = TaskId
        self.SeedList = SeedList

    def KillAll (self, Pid):
        CurProc = psutil.Process(Pid)
        Children = CurProc.children(recursive=True)
        try:
            for ch in Children:
                os.kill(ch.pid, signal.SIGTERM)
            os.kill (Pid, signal.SIGTERM)
        except:
            pass
    
    def RunSeed (self, Seed):
        Cmd = "python -m runone -s " + Seed + " 2>/dev/null"
        SubProc = subprocess.Popen(Cmd, shell=True, stdout=subprocess.PIPE, stderr = subprocess.STDOUT)
        try:
            Results,err  = SubProc.communicate(timeout=20)
            Results = Results.decode("utf-8").split ('\n')
            Len = len (Results)
            if Results[Len-2] != 'True':
                return False
        except TimeoutExpired:
            self.KillAll (SubProc.pid)
            return False
        return True
            
    def run(self):
        FailNum = 0
        par = ProgressBar ()
        for seed in par(self.SeedList):
            Ret = self.RunSeed (seed)
            if Ret == False:
                print ("[CALIBRATING-FAIL]" + seed)
                os.remove (seed)
                FailNum += 1
        print ("[TASK-%d] FailNum = %d" %(self.TaskId, FailNum))

class Calibrate ():
    def __init__ (self, Seedpath):
        self.Run (Seedpath)

    def _GetTests (self, Seedpath):
        AllTests = []
        ModDir = os.walk(Seedpath)
        for Path, Dirs, Pys in ModDir:      
            for py in Pys:
                Mod, Ext = os.path.splitext(py)
                if Ext != ".py":
                    continue
                PyFile = os.path.join(Path, py)
                AllTests.append (PyFile)
        return AllTests

    def Run (self, Seedpath, TaskNum=4):
        AllSeeds = self._GetTests (Seedpath)
        SeedNum  = len (AllSeeds)
        DistNum  = int(SeedNum / TaskNum)

        if SeedNum == 0:
            Rtask = Task (AllSeeds)
            Rtask.run ()
        else:
            SeedNo = 0
            TaskId = 0
            AllTasks = []
            while TaskId < TaskNum:
                EndNo = SeedNo+DistNum
                if TaskId+1 == TaskNum:
                    EndNo = -1
                
                print ("[TASK-%d] calibrating range [%d, %d] / %d" %(TaskId, SeedNo, EndNo, SeedNum))
                RTask = Task (TaskId, AllSeeds[SeedNo:EndNo])
                RTask.start()
                AllTasks.append (RTask)

                SeedNo += DistNum
                TaskId += 1

            for task in AllTasks:
                task.join()
