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


DEFAULT_STMT_NUM = 16

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

        StmtNum = os.environ.get ('SL_STMT_NUM')
        if StmtNum == None:
            self.StmtNum = DEFAULT_STMT_NUM
        else:
            self.StmtNum = int (StmtNum)
            #print ("### CodeGen: obtain SL_STMT_NUM as %d" %self.StmtNum)

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

    def SelectCmd (self, Type, StatNum=0):
        CmdList = None
        if Type == SLCmd.BASE:    
            CmdList = self.BaseCmdList
        elif Type == SLCmd.APP:
            CmdList = self.AppCmdList
        else:
            raise Exception("Unknown CMD Type: " + Type)

        if self.Strategy == CodeGen.STRATEGY_RANDOM:
            CmdIndex = random.randint(0, len (CmdList)-1)
            Cmd = CmdList [CmdIndex]
            if StatNum%Cmd.slCmd.Mod != 0:
                return None
            return Cmd
        elif self.Strategy == CodeGen.STRATEGY_WEIGHT:
            return None
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
        Num = StatNum
        while Num > 0:
            AppCmd = self.SelectCmd (SLCmd.APP, StatNum)
            if AppCmd == None:
                continue
            Ret = self.WriteScript (AppCmd, Ret)

            Num = Num-1

        self.CloseSlHandle ()
        return self.LoadSl (Output)

    def GenPy (self, ApiExpr, StatNum, PyFile, OOFlag=False):
        ScriptFile = 'script.sl'
        Script = self.GenSL (ApiExpr, StatNum, ScriptFile)
        #print (Script)
        self.Core.Run (Script, OutPut=PyFile)

    def DefaultNumber (self):
        Number = os.environ.get ("INIT_SEED_NUM")
        if Number == None:
            return 0xffffff
        else:
            return int (Number)
        
    def IsHoleApi (self, ApiInfo):
        ApiSpec = ApiInfo.Api
        if len (ApiSpec.Args) == 0 and\
           len (ApiSpec.PosArgs) == 0 and\
           len (ApiSpec.KwoArgs) == 0 and\
           len (ApiSpec.Ret) == 0:
            return True
        else:
            return False
        
    def GetApiDir (self, BaseDir, ApiPath):
        ApiName = ApiPath.replace('.', '#')
        ApiDir  = BaseDir + '/' + ApiPath
        if not os.path.exists (ApiDir):
            os.mkdir (ApiDir, mode=0o777)
        return ApiName, ApiDir

    def GenInitPy (self, Dir):
        ApiList = self.Core.ApiList
        InitStatNum = 1
        pbar = ProgressBar()
        PyNum = 0
        MaxNumber = self.DefaultNumber ()
        for ApiPath, ApiInfo in pbar(ApiList.items ()):
            try:
                #if self.IsHoleApi (ApiInfo) == True:
                #    continue
                ApiName, ApiDir = self.GetApiDir (Dir, ApiPath)

                PyFile  =  ApiDir + '/' + str(InitStatNum) + '#' + ApiName + '.py'
                self.GenPy (ApiPath, InitStatNum, PyFile, ApiInfo.Class != None)
            except Exception as e:     
                traceback.print_exc ()
                return None
            PyNum += 1
            if PyNum >= MaxNumber:
                break
        print ("### Generating %d seeds..." %PyNum)
        return Dir

    def GenRandomPy (self, Dir, StateNum=DEFAULT_STMT_NUM):
        try:
            ApiList = list (self.Core.ApiList.keys())
            ApiIndex = random.randint(0, len (ApiList)-1)

            RandomApi = ApiList[ApiIndex]
            ApiInfo = self.Core.ApiList.get (RandomApi)

            StateNum = random.randint(0, StateNum)
            ApiName, ApiDir = self.GetApiDir (Dir, RandomApi)
            PyFile  = ApiDir + '/' + str(StateNum) + '#' + ApiName + '.py'

            self.GenPy (RandomApi, StateNum, PyFile, ApiInfo.Class != None)
        except Exception as e:     
            traceback.print_exc ()
            return None

        print ("Get random API as:" + RandomApi)
        return PyFile

    def GenSpecifiedPy (self, Case, StateNum=DEFAULT_STMT_NUM):
        if self.StmtNum != StateNum:
            StateNum = self.StmtNum
        
        try:
            CaseName = os.path.basename (Case)
            CaseName,_ = os.path.splitext(CaseName)
            ApiIndex = CaseName.find ('#')
            ApiPath = CaseName [ApiIndex+1:].replace ('#', '.')
            print ("ApiPath is " + ApiPath)
            ApiInfo = self.Core.ApiList.get (ApiPath)
            
            PathPrefix = Case.rfind ('/')
            StateNum = random.randint(0, StateNum)
            PyFile  = Case[0:PathPrefix+1] + str(StateNum) + '#' + ApiPath.replace('.', '#') + '.py'

            self.GenPy (ApiPath, StateNum, PyFile, ApiInfo.Class != None)
        except Exception as e:     
            traceback.print_exc ()
            return None
        
        return PyFile

    def UpdateWeight (self, Case, Weight):
        pass

    def GenPyApp (self, ApiPath, StateNum=DEFAULT_STMT_NUM):
        if self.StmtNum != StateNum:
            StateNum = self.StmtNum
        
        ApiInfo = self.Core.ApiList.get (ApiPath)
        if ApiInfo == None:
            print ("Fail to find %s in API spec list!" %ApiPath)
            return
        
        StateNum = random.randint(0, StateNum)
        PyFile   = ApiPath.replace ('.', '#')+'.py'
        self.GenPy (ApiPath, StateNum, PyFile, ApiInfo.Class != None)
        return

