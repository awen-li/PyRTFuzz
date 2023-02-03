import random
from .core import SLCmd

class WtSLCmd ():
    def __init__ (self, slCmd):
        self.slCmd  = slCmd
        self.Weight = 1

    def SetWeight (self, Weight):
        self.Weight = Weight


class ScriptGen ():
    def __init__ (self, CmdList):
        self.CmdList = CmdList

    def InitCmdList (self, SlCmdList):
        pass

    def GenSL (self):
        pass

