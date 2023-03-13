
import sys
import os

def _GetDir ():
    if len (sys.argv) == 1:
        return "."
    else:
        return sys.argv[1]

def Collect (SeedDir='seeds'):
    CurDir = _GetDir ()
    FileList = os.listdir (CurDir)
    for file in FileList:
        pass


if __name__ == '__main__':
    print (sys.argv)
    Collect ()