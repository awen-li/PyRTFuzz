

class HardcodedApi ():
    def __init__ (self):
        self.HdcApi = {}
        self.SetUp ()
    
    def GetTypeList (self, ApiPath):
        return self.HdcApi.get (ApiPath)

    def AddHdcApi (self, ApiPath, TypeList):
        TL = self.HdcApi.get (ApiPath)
        if TL != None:
            print ("[%s] has been set as: %s before!!!" %(ApiPath, str(TL)))
    	
        self.HdcApi[ApiPath] = TypeList
    
    def SetUp (self):
        self.AddHdcApi ('ctypes.macholib.dyld.dyld_env ', ['env:list', 'var:str'])

        
