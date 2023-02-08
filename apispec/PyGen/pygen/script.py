import os
import random
from .core import SLCmd, Core

class WtSLCmd ():
    def __init__ (self, Name, slCmd):
        self.Name   = Name
        self.slCmd  = slCmd
        self.Weight = 1

    def SetWeight (self, Weight):
        self.Weight = Weight


class CodeGen ():
    STRATEGY_RANDOM = 1
    STRATEGY_WEIGHT = 2

    def __init__ (self, ApiSpec, Strategy=STRATEGY_RANDOM):
        self.BaseCmdList = []
        self.AppCmdList  = []
        self.Strategy    = Strategy
        self.SlHandle    = None
        self.Core        = Core (ApiSpec)
        self.InitCmdList (self.Core.GetCmdList ())

    def IsCoreUp (self):
        return self.Core.InitOk

    def InitCmdList (self, SlCmdList):
        for CmdName, SlCmd in SlCmdList.items ():
            WtCmd = WtSLCmd (CmdName, SlCmd)
            if SlCmd.Type == SLCmd.BASE:    
                self.BaseCmdList.append(WtCmd)
            elif SlCmd.Type == SLCmd.APP:
                self.AppCmdList.append(WtCmd)
            else:
                raise Exception("Unknown CMD Type: " + SlCmd.Type)

    def SelectWtCmd (self, CmdList):
        pass

    def SelectCmd (self, Type):
        CmdList = None
        if Type == SLCmd.BASE:    
            CmdList = self.BaseCmdList
        elif Type == SLCmd.APP:
            CmdList = self.AppCmdList
        else:
            raise Exception("Unknown CMD Type: " + Type)

        if self.Strategy == CodeGen.STRATEGY_RANDOM:
            CmdIndex = random.randint(0, len (CmdList)-1)     
            return CmdList [CmdIndex]
        elif self.Strategy == CodeGen.STRATEGY_WEIGHT:
            pass
        else:
            raise Exception("Unknown Strategy Type: " + self.Strategy)

    def InitSlHandle (self, Output):
        if os.path.exists (Output):
            os.remove (Output)
        
        self.SlHandle = open (Output, 'a+')
        if self.SlHandle == None:
            raise Exception("Create script fail: " + Output)

    def CloseSlHandle (self):
        self.SlHandle.close ()
    
    def WriteScript (self, Cmd, Input):
        Ret = 'p'
        print ('%s = %s (%s)' %(Ret, Cmd.Name, Input) , file=self.SlHandle)
        return Ret

    def LoadSl (self, SlFile='script.sl'):
        with open (SlFile, 'r') as f:
            Script = f.read()
            return Script

    def GenSL (self, ApiExpr, StatNum, Output='script.sl'):
        self.InitSlHandle (Output)

        # 1. select a BASE CMD
        BaseCmd = self.SelectCmd (SLCmd.BASE)
        Ret = self.WriteScript (BaseCmd, ApiExpr)

        # 2. SELECT a set of APP CMD
        while StatNum > 0:
            AppCmd = self.SelectCmd (SLCmd.APP)
            Ret = self.WriteScript (AppCmd, Ret)

            StatNum = StatNum-1

        self.CloseSlHandle ()
        return self.LoadSl (Output)

    def GenPy (self, ApiExpr, StatNum, PyFile='pyapp.py'):
        ScriptFile = 'script.sl'
        Script = self.GenSL (ApiExpr, StatNum, ScriptFile)
        print (Script)

        self.Core.Run (Script, OutPut=PyFile)

    def GenInitPy (self, Dir):
        return Dir

    def GenRandomPy (self, Dir):
        return Dir

    def GenWeightedPy (self, Dir):
        return Dir

    def UpdateWeight (self, Case):
        pass

