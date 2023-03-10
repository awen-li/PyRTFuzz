
import os
import sys
import psutil
import signal
import time
from fuzzwrap import *
from multiprocessing import Process
from datetime import datetime

LOG_DIR = 'fuzzlog/'

def _Log ():
    if not os.path.exists (LOG_DIR):
        os.mkdir (LOG_DIR, mode=0o777)
    LogFile = LOG_DIR + 'pyfuzz.log'

    try:
        with open(LogFile, 'a') as LogF:
            LastApp = ''
            with open('CURRENT-level-fuzzing.log', 'r') as LF:
                LastApp = LF.readline()
            CurTime = str(datetime.now())
            print (f"[{CurTime}]\t{LastApp}", file=LogF)
    except:
        pass

if __name__ == '__main__':
    IterNum = 0
    while True:
        Fuzzer = Process(target=FuzzEntry, args=())
        Fuzzer.start()
        print ("\n### [%d]Fuzzer process starts [%d]\n" %(IterNum, Fuzzer.pid))

        time.sleep(15)
        CurProc = psutil.Process(Fuzzer.pid)
        ChildProc = CurProc.children(recursive=True)

        Fuzzer.join ()
        print ("\n\n### [%d]Fuzzer process exit [%d]\n" %(IterNum, Fuzzer.pid))
        IterNum += 1
        _Log ()

        try:
            for proc in ChildProc:
                if psutil.Process(proc.pid) != None:
                    os.kill(proc.pid, signal.SIGTERM)
        except:
            pass


 
