
import sys
import os
from shutil import copyfile

def _GetDir ():
    if len (sys.argv) == 1:
        return "."
    else:
        return sys.argv[1]
    
def _GetAppName (file):
    if file[0:6] == 'crash-':
        End = file.rfind ("-")
        return file[6:End]
    elif file[0:10] == 'slow-unit-':
        End = file.rfind ('-')
        return file[10:End]
    else:
        return None

def _GetAppDir (CurDir, SeedDir, AppName):
    Sindex = AppName.find ('#')
    Eindex = AppName.rfind ('.')
    AppName = AppName[Sindex+1:Eindex].replace('#', '.')
    AppDir = os.path.join(CurDir, SeedDir, AppName)
    if os.path.exists (AppDir) == True:
        return AppDir
    else:
        print (AppDir + " is not a valid path!!!!")
        return None
    
def MoveTo (file, TargetDir='FuzzResult'):
    if os.path.isfile (file) == False:
        return
    
    if os.path.exists (TargetDir) == False:
        os.mkdir (TargetDir, mode=0o777)

    FileName = os.path.basename (file)
    try:
        copyfile(file, TargetDir+'/'+FileName)
    except:
        print("Unable to copy file. %s" %file)


def Collect (SeedDir='seeds'):
    CurDir = _GetDir ()
    FileList = os.listdir (CurDir)
    AppNum = 0
    for file in FileList:
        AppName = _GetAppName (file)
        if AppName == None:
            continue
        AppDir = _GetAppDir (CurDir, SeedDir, AppName)    
        App = os.path.join(AppDir, AppName)
        Test = os.path.join(CurDir, file)
        MoveTo (App)
        MoveTo (Test)
        AppNum += 1
    print ("### [Collect] Total %d APP & test get collected...." %AppNum)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        Collect (sys.argv[1])
    else:
        Collect ()