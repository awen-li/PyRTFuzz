

debugFlag = True

def SetDebug (Flag=False):
    Debug.debugFlag = Flag

def DebugPrint (Msg, end='\n'):
    if debugFlag == True:
        print ('[DEBUG]' + Msg)
                
                
        

        


