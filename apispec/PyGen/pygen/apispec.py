
# _*_ coding:utf-8 _*_
from xml.dom.minidom import parse
import xml.dom.minidom
from .debug import *

"""
<?xml version="1.0" ?>
<apisepc version="1.0">
    <library name="email">
        <module name="charset">
            <class name="Charset" init="obj = Charset()" args="">
                <api name="get_body_encoding">
                        <expr>ret = get_body_encoding()</expr>
                        <parameters>{}</parameters>
                        <return>{'ret':base64|7bit}</return>
                        <dependences>  </dependences>
                </api>

                <api name="header_encode">
                        <expr>header_encode(str)</expr>
                        <parameters>{'str':string}</parameters>
                        <return>{}</return>
                        <dependences>  </dependences>
                </api>
            </class>
        </module>

        <module name="contentmanager">
            <api name="header_encode">
                <expr>header_encode(str)</expr>
                <parameters>{'str':string}</parameters>
                <return>{}</return>
                <dependences>  </dependences>
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
class PyApi ():
    def __init__ (self, ApiName, Expr, Ret, Parameters, Dependences):
        self.ApiName = ApiName
        self.Expr    = Expr
        self.Ret     = Ret
        self.Parameters = Parameters
        self.Dependences = Dependences
        

class PyCls ():
    def __init__ (self, clsName, Init):
        self.clsName = clsName
        self.clsInit = Init
        self.Apis = {}


class PyMod ():
    def __init__ (self, mdName):
        self.mdName  = mdName
        self.Apis    = {}
        self.Classes = {}

class PyExcep ():
    def __init__ (self, exName):
        self.exName  = exName

        
class PyLib ():
    def __init__ (self, Name):
        self.Name  = Name
        self.Modules = {}
        self.Exceptions = []

        
class ApiSpec():
    def __init__(self, apiSpecXml='apispec.xml'):
        self.apiSpecXml = apiSpecXml
        self.PyLibs = {}

        self.apiAddr = {}

    def AssertAttr (self, node, attr):
        if not node.hasAttribute(attr):
            print ("Node item has no attribute %s!" %attr)
            exit (0)

    def ParseApi (self, apiName, xmlApi):
        DebugPrint ("apiName = " + apiName)
        expr = xmlApi.getElementsByTagName("expr")[0].childNodes[0].data
        DebugPrint ("\t: expr-> " + expr)
        parameters = xmlApi.getElementsByTagName("parameters")[0].childNodes[0].data
        DebugPrint ("\t: parameters-> " +parameters)
        ret = xmlApi.getElementsByTagName("return")[0].childNodes[0].data
        DebugPrint ("\t: ret-> " + ret)
        dependences = xmlApi.getElementsByTagName("dependences")[0].childNodes[0].data
        DebugPrint ("\t: dependences-> " + dependences)

        return PyApi (apiName, expr, eval(ret), eval(parameters), dependences)

    def ParseExceps (self, pyLib, xmlExp):
        xmlExpList = xmlExp[0].getElementsByTagName("exception")
        for xExp in xmlExpList:
            exp = xExp.childNodes[0].data
            pyLib.Exceptions.append (exp)
            DebugPrint (exp)

    def ParseClass (self, clsName, clsInit, xmlCls):
        curCls = PyCls (clsName, clsInit)
        
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
            DebugPrint ("# Parse class: " + clsName + " -> [init]"  + clsInit)
                                   
            curMd.Classes [clsName] = self.ParseClass (clsName, clsInit, xmlCls)

        # api under module
        xmlApis = xmlMd.getElementsByTagName ("api")
        for xmlApi in xmlApis:
            if self.apiAddr.get (xmlApi) != None:
                continue
            apiName = xmlApi.getAttribute("name")
            curMd.Apis [apiName] = self.ParseApi (apiName, xmlApi)

        self.apiAddr = {}
        return curMd
            
    def Parser (self):
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
                curMod = self.ParseMod (mdName, xmlMd)
                curLib.Modules [mdName] = curMod

            # exception under library
            xmlExceps = xmlLib.getElementsByTagName ("errors")
            self.ParseExceps (curLib, xmlExceps)
                
               

      