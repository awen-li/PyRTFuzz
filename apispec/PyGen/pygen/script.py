import random
from .core import SLCmd

class WtSLCmd ():
    def __init__ (self, slCmd):
        self.slCmd  = slCmd
        self.Weight = 1

    def SetWeight (self, Weight):
        self.Weight = Weight


class ScriptGen ():
    STRATEGY_RANDOM = 1
    STRATEGY_WEIGHT = 2

    def __init__ (self, Strategy=STRATEGY_RANDOM):
        self.BaseCmdList = {}
        self.AppCmdList  = {}
        self.Strategy    = Strategy

    def InitCmdList (self, SlCmdList):
        for CmdName, SlCmd in SlCmdList.items ():
            WtCmd = WtSLCmd (SlCmd)
            if SlCmd.Type == SLCmd.BASE:    
                self.BaseCmdList [CmdName] = WtCmd
            elif SlCmd.Type == SLCmd.APP:
                self.AppCmdList [CmdName] = WtCmd
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

        if self.Strategy == ScriptGen.STRATEGY_RANDOM:
            CmdIndex = random.randint(0, len (CmdList)-1)     
            return CmdList [CmdIndex]
        elif self.Strategy == ScriptGen.STRATEGY_WEIGHT:
            pass
        else:
            raise Exception("Unknown Strategy Type: " + self.Strategy)

    def GenSL (self, ApiExpr):
        # 1. select a BASE CMD
        BaseCmd = self.SelectCmd (SLCmd.BASE)

        # 2. SELECT a set of APP CMD

