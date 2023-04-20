
import sys
import os
from shutil import copyfile

HisSeedLog = "History.hty"
HisSeed = []

def _LoadHisSeeds (File=HisSeedLog):
    try:
        with open (File, "r") as F:
            AllNames = F.readlines ()
            for Name in AllNames:
                Name = Name.replace ('\n', '')
                if Name in HisSeed:
                    continue
                HisSeed.append (Name)
    except:
        pass

def _App2HisRec (AppName):
    S = AppName.find ("#")
    if S == None:
        return
    Hisrec = '1' + AppName[S:]
    if len (Hisrec) < 8:
        return
    if not Hisrec in HisSeed:
        HisSeed.append (Hisrec)

def _SaveHisSeeds (File=HisSeedLog):
    with open (File, "w") as F:
        for Name in HisSeed:
            F.write(Name+'\n')
    
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
    _LoadHisSeeds ()

    CurDir = '.'
    FileList = os.listdir (CurDir)
    AppNum = 0
    for file in FileList:
        AppName = _GetAppName (file)
        if AppName == None:
            continue

        _App2HisRec (AppName)

        if os.path.exists (SeedDir) == False:
            continue
        
        AppDir = _GetAppDir (CurDir, SeedDir, AppName)
        if AppDir == None:
            continue 
        App = os.path.join(AppDir, AppName)
        Test = os.path.join(CurDir, file)
        MoveTo (App)
        MoveTo (Test)
        AppNum += 1
        try:
            os.remove (Test)
        except:
            pass
    print ("### [Collect] Total %d APP & test get collected...." %AppNum)

    Log = "PRTFuzz_perf.log"
    if os.path.exists (Log) == True:
        MoveTo (Log)

    _SaveHisSeeds ()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        Collect (sys.argv[1])
    else:
        Collect ()