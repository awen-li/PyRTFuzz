

class AppTmpt ():
    def __init__ (self):
        self.TmptList = []

    def Add (self, tmpt):
        self.TmptList.append (tmpt)


ATs = AppTmpt ()

def InitTmpts ():
    ATs.Add (
    """
class demoCls:
    def __init__(self):
        pass

    def demoFunc1(self, arg1):
        pass

def RunFuzzer (x):
    dc = demoCls ()
    dc.demoFunc1 (x)
    """
    )

    ATs.Add (
    """
def demoFunc1 (arg1):
    pass

def RunFuzzer (x):
    demoFunc1 (x)
    """
    )

InitTmpts ()