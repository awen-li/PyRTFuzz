import os
import argparse
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
    for test in AllTests:
        AppName = _GetAppName (test)
        AppPath = os.path.join (opts.dirname, AppName)

        print ("### Running " + AppPath + ' with input: ' + test)
        with open (test, 'r') as F:
            Inputs = F.read ()
            RunScript (AppPath, Input=Inputs)

if __name__ == "__main__":
   main()

