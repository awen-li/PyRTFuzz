import os
import argparse
import psutil
import signal
from fuzzwrap import *

def _GetAllTests (DirName):
    AllTests = []
    FileList = os.listdir (DirName)
    for file in FileList:
        Path = os.path.join (DirName, file)
        if os.path.isdir (Path):
            continue

        if Path.find ("slow-unit-") != -1 or Path.find ("crash-1") != -1:
            AllTests.append (Path)
    return AllTests

def _GetAppName (Test):
    file = os.path.basename (Test)
    if file[0:6] == 'crash-':
        End = file.rfind ("-")
        return file[6:End]
    elif file[0:10] == 'slow-unit-':
        End = file.rfind ('-')
        return file[10:End]
    else:
        return None
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dirname', nargs='?', help='the dir for running fuzzing tests')
    parser.add_argument('arguments', nargs=argparse.REMAINDER, help='arguments to the program')

    opts = parser.parse_args()
    if opts.dirname is None:
        parser.error('please specify the dirname!')
    
    AllTests = _GetAllTests (opts.dirname)
    Id = 0
    All = len (AllTests)
    for Test in AllTests:
        RunTest (Id, All, opts.dirname, Test)
        Id += 1

def RunOne (Id, All, Dir, Test):
    AppName = _GetAppName (Test)
    AppPath = os.path.join (Dir, AppName)

    print ("### [%3d/%3d] Running %s with input: %s" %(Id, All, AppPath, Test))
    with open (Test, 'rb') as F:
        Inputs = F.read ()
        RunScript (AppPath, Input=Inputs, Silent=True)

def RunTest (Id, All, Dir, Test, TimeOut=180):
    Rp = Process(target=RunOne, args=(Id, All, Dir, Test,))
    Rp.start()
    Rp.join (TimeOut)

    try:
        if psutil.Process(Rp.pid) != None:
            os.kill(Rp.pid, signal.SIGTERM)
            print ("\n\t Running timeout (over %d s)!\n" %(TimeOut))
    except psutil.NoSuchProcess:
        pass


if __name__ == "__main__":
   main()

