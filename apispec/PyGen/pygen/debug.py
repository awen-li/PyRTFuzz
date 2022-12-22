import os

DEBUG_ENV = 'pygen_debug'

debugFlag = os.environ.get (DEBUG_ENV)
if debugFlag == None:
    debugFlag = 0
else:
    debugFlag = int (debugFlag)


def SetDebug (Flag=0):
    os.environ[DEBUG_ENV] = str(Flag)
    print ("[DEBUG] set debug to %d" %Flag)

def DebugPrint (Msg, end='\n'):
    if debugFlag == True:
        print ('[DEBUG]' + Msg)
                
                
        

        


