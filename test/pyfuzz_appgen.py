from pygen import *

Spec = '../experiments/apispec.xml'

CG = CodeGen (Spec)
APIexpr = "http.cookiejar.http2time"


def GenSL (BaseCmd, AppCmd, SL='script.sl'):
    CG.InitSlHandle (SL)
    Ret = CG.WriteScript (BaseCmd, APIexpr)
    Ret = CG.WriteScript (AppCmd, Ret)
    CG.CloseSlHandle ()
    return CG.LoadSl (SL)

BaseCmd = CG.SelectCmd (SLCmd.BASE)
for AppCmd in CG.AppCmdList:
    print ("### Generate APP with CMD:%-16s for %s" %(AppCmd.Name, APIexpr))
    SL = GenSL (BaseCmd, AppCmd)
    CG.Core.Run (SL, OutPut='sl2python.py')