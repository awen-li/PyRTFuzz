import os

DEBUG_ENV = 'PYDEBUG'


global debugFlag


def LoadFlag ():
    dFlag = os.environ.get (DEBUG_ENV)
    if dFlag == None:
        dFlag = 0
    else:
        dFlag = int (dFlag)
    return dFlag

def SetDebug (Flag=0):
    os.environ[DEBUG_ENV] = str(Flag)
    debugFlag = LoadFlag ()
    print ("[DEBUG] set debug to %d" %debugFlag)

def DebugPrint (Msg, end='\n'):
    debugFlag = LoadFlag () 
    if debugFlag == True:
        print ('[DEBUG]' + Msg)
                
                
        
debugFlag = LoadFlag ()

        


