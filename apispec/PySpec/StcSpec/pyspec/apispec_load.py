
import os
import xml.dom.minidom
from xml.dom.minidom import parse
from .apispec import *

DebugFlag = os.environ.get ("PYDEBUG")
def DebugPrint (Msg, end='\n'):
    if DebugFlag == True:
        print ('[DEBUG]' + Msg)

"""
<?xml version="1.0" ?>
<apisepc version="1.0">
    <library name="email">
        <module name="charset">
            <class name="Charset" init="obj = Charset()">
                <api name="get_body_encoding">
                        <expr>ret = get_body_encoding()</expr>
                        <args>[]</args>
                        <return>{'ret:base64|7bit'}</return>
                        <dependences>  </dependences>
                        <posargs>[]</posargs>
                        <kwoargs>[]</kwoargs>
                </api>

                <api name="header_encode">
                        <expr>header_encode(str)</expr>
                        <parameters>['str:string']</parameters>
                        <return>{}</return>
                        <dependences>  </dependences>
                        <posargs>[]</posargs>
                        <kwoargs>[]</kwoargs>
                </api>
            </class>
        </module>

        <module name="contentmanager">
            <api name="header_encode">
                <expr>header_encode(str)</expr>
                <args>['str:string']</args>
                <return>{}</return>
                <dependences>  </dependences>
                <posargs>[]</posargs>
                <kwoargs>[]</kwoargs>
            </api>
        </module >

        <errors>
            <exception>MessageError</exception>
            <exception>MessageParseError</exception>
            <exception>BoundaryError</exception>
            <exception>MultipartConversionError</exception>
        </errors>
    </library>
</apisepc>
"""
        
class ApiSpecLoader():
    def __init__(self, apiSpecXml='apispec.xml'):
        self.apiSpecXml = apiSpecXml
        self.PyLibs = {}
        self.apiAddr = {}

    @staticmethod
    def Show (PyLibs):
        print ("\n\n=========================== ShowSpec ===========================")
        for libName, pyLib in PyLibs.items ():
            print ("# LIB: " + libName)
            for mdname, md in pyLib.Modules.items ():
                print ("## MOD: " + mdname)
                for clsname, cls in md.Classes.items ():
                    print ("### CLASS: " + clsname)
                    for apiname, api in cls.Apis.items ():
                        print ("#### API: " + apiname + " == Args: " + str(api.Args) + " Ret: " + str(api.Ret))

                for apiname, api in md.Apis.items ():
                    print ("#### API: " + apiname + " == Args: " + str(api.Args) + " Ret: " + str(api.Ret))
        print ("=========================== ShowSpec end ========================\n\n")
        
    def AssertAttr (self, node, attr):
        if not node.hasAttribute(attr):
            print ("Node item has no attribute %s!" %attr)
            exit (0)

    def ParseApi (self, apiName, xmlApi):
        DebugPrint ("apiName = " + apiName)
        expr = xmlApi.getElementsByTagName("expr")[0].childNodes[0].data
        DebugPrint ("\t: expr-> " + expr)
        parameters = xmlApi.getElementsByTagName("args")[0].childNodes[0].data
        DebugPrint ("\t: args-> " +parameters)
        ret = xmlApi.getElementsByTagName("return")[0].childNodes[0].data
        DebugPrint ("\t: ret-> " + ret)
        dependences = xmlApi.getElementsByTagName("dependences")[0].childNodes[0].data
        DebugPrint ("\t: dependences-> " + dependences)

        posagrs = xmlApi.getElementsByTagName("posargs")[0].childNodes[0].data
        DebugPrint ("\t: posagrs-> " + posagrs)
        kwoargs = xmlApi.getElementsByTagName("kwoargs")[0].childNodes[0].data
        DebugPrint ("\t: kwoargs-> " + kwoargs)

        defas = xmlApi.getElementsByTagName("defa")[0].childNodes[0].data
        DebugPrint ("\t: default args-> " + defas)
        kwodefas = xmlApi.getElementsByTagName("kwodefa")[0].childNodes[0].data
        DebugPrint ("\t: default kwoargs-> " + kwodefas)
        
        return PyApi (apiName, expr, eval(ret), eval(parameters), eval(posagrs), eval(kwoargs), eval(defas), eval(kwodefas), dependences)

    def ParseExceps (self, pyLib, xmlExp):
        if len (xmlExp) == 0:
            if DebugFlag != None:
                print ("Warning: %s extracted none exceptions!!!\r\n" %pyLib.Name)
            return
            
        xmlExpList = xmlExp[0].getElementsByTagName("exception")
        for xExp in xmlExpList:
            exp = xExp.childNodes[0].data
            pyLib.Exceptions.append (PyExcep(exp))
            DebugPrint (exp)

    def ParseClass (self, xmlCls, clsName, clsInit, clsBase):
        curCls = PyCls (clsName, clsInit, clsBase)
        
        xmlApis = xmlCls.getElementsByTagName("api")
        for xmlApi in xmlApis:
            self.apiAddr [xmlApi] = True
            
            apiName = xmlApi.getAttribute("name")
            curCls.Apis[apiName] = self.ParseApi (apiName, xmlApi)
        
        return curCls

    def ParseMod (self, mdName, xmlMd):
        DebugPrint ("# Parse module: " + mdName)
        curMd = PyMod (mdName)

        # class under modules
        xmlClasses = xmlMd.getElementsByTagName ("class")
        for xmlCls in xmlClasses:          
            self.AssertAttr (xmlCls, "name")
            clsName = xmlCls.getAttribute("name")
            clsInit = xmlCls.getAttribute("init")
            clsBase = xmlCls.getAttribute("base")
            if len (clsBase) == 0:
                clsBase = None
            DebugPrint ("# Parse class: " + clsName + " -> [init]"  + clsInit)
                                   
            curMd.Classes [clsName] = self.ParseClass (xmlCls, clsName, clsInit, clsBase)

        # api under module
        xmlApis = xmlMd.getElementsByTagName ("api")
        for xmlApi in xmlApis:
            if self.apiAddr.get (xmlApi) != None:
                continue
            apiName = xmlApi.getAttribute("name")
            curMd.Apis [apiName] = self.ParseApi (apiName, xmlApi)
        self.apiAddr = {}

        #exception under module
        xmlExceps = xmlMd.getElementsByTagName ("errors")
        self.ParseExceps (curMd, xmlExceps)
            
        return curMd
            
    def Parser (self):
        if self.apiSpecXml == None or os.path.exists (self.apiSpecXml) == False:
            return
        
        DOMTree = xml.dom.minidom.parse(self.apiSpecXml)
        De = DOMTree.documentElement
        self.AssertAttr (De, "version")     

        xmlLibs = De.getElementsByTagName("library")
        for xmlLib in xmlLibs:
    
            self.AssertAttr (xmlLib, "name")
            libName = xmlLib.getAttribute("name")
            DebugPrint ("# Parse library:  " + libName)
            curLib = PyLib (libName)
            self.PyLibs [libName] = curLib

            xmlModules = xmlLib.getElementsByTagName ("module")
            for xmlMd in xmlModules:
            
                self.AssertAttr (xmlMd, "name")
                mdName = xmlMd.getAttribute("name")
                Imports = xmlMd.getAttribute("imports")
                ImportFrom = xmlMd.getAttribute("importfrom")

                curMod = self.ParseMod (mdName, xmlMd)
                curMod.Imports = eval (Imports)
                curMod.ImportFrom = eval (ImportFrom)
                
                curLib.Modules [mdName] = curMod

                
               

      