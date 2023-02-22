import os
import sys
import random
import traceback
from progressbar import ProgressBar
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
        try:
            self.Core    = Core (ApiSpec)
        except:
            traceback.print_exc ()
            sys.exit (0)
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

    def GenSL (self, ApiExpr, StatNum, Output='script.sl', OOFlag=False):
        self.InitSlHandle (Output)

        # 1. select a BASE CMD
        while True:
            BaseCmd = self.SelectCmd (SLCmd.BASE)
            if OOFlag == False and BaseCmd.slCmd.OORequired == True:
                continue
            else:
                break
        Ret = self.WriteScript (BaseCmd, ApiExpr)

        # 2. SELECT a set of APP CMD
        while StatNum > 0:
            AppCmd = self.SelectCmd (SLCmd.APP)
            Ret = self.WriteScript (AppCmd, Ret)

            StatNum = StatNum-1

        self.CloseSlHandle ()
        return self.LoadSl (Output)

    def GenPy (self, ApiExpr, StatNum, PyFile, OOFlag=False):
        ScriptFile = 'script.sl'
        Script = self.GenSL (ApiExpr, StatNum, ScriptFile)
        #print (Script)
        self.Core.Run (Script, OutPut=PyFile)

    def DefaultNumber (self):
        Number = os.env.get ("INIT_SEED_NUM")
        if Number == None:
            return 0xffffff
        else:
            return int (Number)

    def GenInitPy (self, Dir):
        ApiList = self.Core.ApiList
        InitStatNum = 1
        pbar = ProgressBar()
        PyNum = 0
        MaxNumber = self.DefaultNumber ()
        for ApiPath, ApiInfo in pbar(ApiList.items ()):
            PyFile  = Dir + '/' + str(InitStatNum) + '#' + ApiPath.replace('.', '#') + '.py'
            
            try:
                self.GenPy (ApiPath, InitStatNum, PyFile, ApiInfo.Class != None)
            except Exception as e:     
                traceback.print_exc ()
                return None
            PyNum += 1
            if PyNum >= MaxNumber:
                break
        print ("### Generating %d seeds..." %PyNum)
        return Dir

    def GenRandomPy (self, Dir, StateNum=16):
        try:
            ApiList = list (self.Core.ApiList.keys())
            ApiIndex = random.randint(0, len (ApiList)-1)

            RandomApi = ApiList[ApiIndex]
            ApiInfo = self.Core.ApiList.get (RandomApi)

            StateNum = random.randint(0, StateNum)
            PyFile  = Dir + '/' + str(StateNum) + '#' + RandomApi.replace('.', '#') + '.py'

            self.GenPy (RandomApi, StateNum, PyFile, ApiInfo.Class != None)
        except Exception as e:     
            traceback.print_exc ()
            return None

        print ("Get random API as:" + RandomApi)
        return PyFile

    def GenSpecifiedPy (self, Case, StateNum=16):
        try:
            Path, Ext = os.path.splitext(Case)

            ApiIndex = Path.find ('#')
            ApiPath = Path [ApiIndex+1:].replace ('#', '.')
            print ("ApiPath is " + ApiPath)
            ApiInfo = self.Core.ApiList.get (ApiPath)
            
            PathPrefix = Path.rfind ('/')
            StateNum = random.randint(0, StateNum)
            PyFile  = Path[0:PathPrefix+1] + str(StateNum) + '#' + ApiPath.replace('.', '#') + '.py'

            self.GenPy (ApiPath, StateNum, PyFile, ApiInfo.Class != None)
        except Exception as e:     
            traceback.print_exc ()
            return None
        
        return PyFile

    def UpdateWeight (self, Case, Weight):
        pass

    def GenPyApp (self, ApiPath, StateNum=16):
        ApiInfo = self.Core.ApiList.get (ApiPath)
        if ApiInfo == None:
            print ("Fail to find %s in API spec list!" %ApiPath)
            return
        
        StateNum = random.randint(0, StateNum)
        PyFile   = ApiPath.replace ('.', '#')+'.py'
        self.GenPy (ApiPath, StateNum, PyFile, ApiInfo.Class != None)
        return

