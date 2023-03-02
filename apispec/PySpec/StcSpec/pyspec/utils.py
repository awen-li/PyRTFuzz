import os
import subprocess

OsExcepts = ["ValueError", "TypeError", "AttributeError"]

def RunCmd (Cmd):
    SubProc = subprocess.Popen(Cmd, shell=True, stdout=subprocess.PIPE, stderr = subprocess.STDOUT)
    Vres = SubProc.stdout.readlines()
    if len (Vres) == 0:
        return ''
    Vres = [line.decode("utf-8").replace ("\n", "") for line in Vres]

    return Vres[-1]


def WriteValidate (Path2Imports, ValidatedApiList, Class2Bases):
    with open ('validate.py', 'w') as F:
        print ('###################################################', file=F)
        print ('# !!!!! This file is generated automatically       ', file=F)
        print ('###################################################\n\n\n', file=F)

        P2Impts = dict(sorted (Path2Imports.items()))
        print ('Path2Imports = {\\', file=F)
        for path, imports in P2Impts.items ():
            print ('\'%s\':\'%s\',\\' %(path, imports), file=F)
        print ('}\n\n', file=F)

        ValidatedApiList.sort ()
        print ('ValidatedApiList = [\\', file=F)
        for ApiPath in ValidatedApiList:
            print ('\'%s\',\\' %(ApiPath), file=F)
        print (']\n\n', file=F)

        C2B = dict(sorted (Class2Bases.items()))
        print ('Class2Bases = {\\', file=F)
        for clsPath, Bases in C2B.items():
            print ('\'%s\':\'%s\',\\' %(clsPath, Bases), file=F)
        print ('}\n\n', file=F)
    return



    