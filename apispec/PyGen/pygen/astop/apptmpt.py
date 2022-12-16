

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
    demoCls ().demoFunc1 (x)
    """
    )

InitTmpts ()