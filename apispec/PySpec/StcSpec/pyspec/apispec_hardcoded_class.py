

class HardcodedCls ():
    def __init__ (self):
        self.HdcCls = {}
        self.SetUp ()

    def GetDefaults (self, ClsPath):
        return self.HdcCls.get (ClsPath)

    def AddHdcCls (self, ClsPath, Defaults):
        DF = self.HdcApi.get (ClsPath)
        if DF != None:
            print ("[%s] has been set as: %s before!!!" %(ClsPath, str(DF)))
    	
        self.HdcApi[ClsPath] = Defaults
    
    def SetUp (self):
        self.AddHdcCls ('xmlrpc.client.ExpatParser', [None])
