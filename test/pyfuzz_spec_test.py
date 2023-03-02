from pygen import *

APISPEC = '../experiments/apispec.xml'

pyGener = Core (APISPEC)
ApiList = pyGener.ApiList
ClassList = pyGener.ClassInfo
ModuleList = pyGener.ModuleList

class SpecTest ():
    def __init__ (self):
        self.TestNum = 0
        self.FailNum = 0
        self.TestEntry ()

    def Assert (self, Cond, Msg):
        self.TestNum += 1
        if Cond == True:
            print ("[SUCCESS]: %s" %Msg)
        else:
            self.FailNum += 1
            print ("[FAIL]: %s" %Msg)

    def TestSet (self):
        print ("Empty TestSet")

    def TestEntry (self):
        self.TestSet ()
        print ("### TOTAL TESTS: %d, FAIL TESTS: %d\n\n" %(self.TestNum, self.FailNum))


class ApiTest (SpecTest):
    def __init__ (self):
        super(ApiTest, self).__init__()

    def AssertApi (self, ApiPath, Expr, Args):
        print ("### TESTING api " + ApiPath)
        Spec = ApiList.get (ApiPath)
        self.Assert (Spec != None, f"get spec {ApiPath}")

        if Spec == None:
            return

        Api = Spec.Api
        self.Assert (Api.Expr==Expr, f"{ApiPath}-expr: {Api.Expr}, expected: {Expr}")
        self.Assert (str(Api.Args)==Args, f"{ApiPath}-args: {Api.Args}, expected: {Args}")
        print ("")
    
    def TestSet (self):
        self.AssertApi ("sqlite3.dbapi2.DateFromTicks", "ret = sqlite3.dbapi2.DateFromTicks(ticks)%%['int']", "['ticks:int']")

class ClsTest (SpecTest):
    def __init__ (self):
        super(ClsTest, self).__init__()

    def AssertClass (self, Cls, Init, Base):
        print ("### TESTING class " + Cls)
        ClsSpec = ClassList.get (Cls)
        self.Assert (ClsSpec != None, f"get spec {Cls}")

        if ClsSpec == None:
            return

        self.Assert (ClsSpec.clsInit==Init, f"{Cls}-expr: {ClsSpec.clsInit}, expected: {Init}")
        self.Assert (ClsSpec.Base==Base, f"{Cls}-args: {ClsSpec.Base}, expected: {Base}")
        print ("")
    
    def TestSet (self):
        self.AssertClass ('HTMLParser', "obj = html.parser.HTMLParser()%%[]", "_markupbase.ParserBase")

class MdTest (SpecTest):
    def __init__ (self):
        super(MdTest, self).__init__()

    def AssertMoudle (self, Md, Imports, ImportFrom):
        print ("### TESTING moudle " + Md)
        MdSpec = ModuleList.get (Md)
        self.Assert (MdSpec != None, f"get spec {Md}")

        if MdSpec == None:
            return

        self.Assert (str(MdSpec.Imports)==Imports, f"{Md}-Imports: {MdSpec.Imports}, expected: {Imports}")
        self.Assert (str(MdSpec.ImportFrom)==ImportFrom, f"{Md}-ImportFrom: {MdSpec.ImportFrom}, expected: {ImportFrom}")
        print ("")
    
    def TestSet (self):
        self.AssertMoudle ("html.parser", "['html', 'html.parser', 're']", "['html:unescape']")
    

if __name__ == "__main__":
    MdTest ()
    ClsTest ()
    ApiTest ()
    