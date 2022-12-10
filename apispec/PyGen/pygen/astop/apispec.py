
# _*_ coding:utf-8 _*_
from xml.dom.minidom import parse
import xml.dom.minidom

"""
<?xml version="1.0" ?>
<apisepc version="1.0">
    <library name="email">
        <module name="charset">
            <class name="Charset">
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
        self.Ret     = {}
        self.Parameters = []
        self.Dependences = Dependences


class PyCls ():
    def __init__ (self, clsName):
        self.clsName  = clsName
        self.Apis = {}


class PyMod ():
    def __init__ (self, mdName):
        self.mdName  = mdName
        self.Apis    = {}
        self.Classes = {}
        self.Exceps  = {}

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
        self.PyLib = {}

        self.apiAddr = {}

    def AssertAttr (self, node, attr):
        if not node.hasAttribute(attr):
            print ("Node item has no attribute %s!" %attr)
            exit (0)

    def ParseApi (self, apiName, xmlApi):
        print ("apiName = %s" %apiName)
        expr = xmlApi.getElementsByTagName("expr")
        print ("\t: expr-> %s" %expr[0].childNodes[0].data)
        parameters = xmlApi.getElementsByTagName("parameters")
        print ("\t: parameters-> %s" %parameters[0].childNodes[0].data)
        ret = xmlApi.getElementsByTagName("return")
        print ("\t: ret-> %s" %ret[0].childNodes[0].data)
        dependences = xmlApi.getElementsByTagName("dependences")
        print ("\t: dependences-> %s" %dependences[0].childNodes[0].data)

        return PyApi (apiName, expr, ret, parameters, dependences)

    def ParseExceps (self, pyLib, xmlExp):
        xmlExpList = xmlExp[0].getElementsByTagName("exception")
        for xExp in xmlExpList:
            exp = xExp.childNodes[0].data
            pyLib.Exceptions.append (exp)
            print (exp)

    def ParseClass (self, clsName, xmlCls):
        curCls = PyCls (clsName)
        
        xmlApis = xmlCls.getElementsByTagName("api")
        for xmlApi in xmlApis:
            self.apiAddr [xmlApi] = True
            
            apiName = xmlApi.getAttribute("name")
            curCls.Apis[apiName] = self.ParseApi (apiName, xmlApi)

    def ParseMod (self, mdName, xmlMd):
        print ("# Parse module: %s" %mdName)
        curMd = PyMod (mdName)

        # class under modules
        xmlClasses = xmlMd.getElementsByTagName ("class")
        for xmlCls in xmlClasses:          
            self.AssertAttr (xmlCls, "name")
            clsName = xmlCls.getAttribute("name")
            print ("# Parse class: %s" %clsName)
                                   
            curMd.Classes [clsName] = self.ParseClass (clsName, xmlCls)

        # api under module
        xmlApis = xmlMd.getElementsByTagName ("api")
        for xmlApi in xmlApis:
            if self.apiAddr.get (xmlApi) != None:
                continue
            apiName = xmlApi.getAttribute("name")
            curMd.Apis [apiName] = self.ParseApi (apiName, xmlApi)

        self.apiAddr = {}
            
    def Parser (self):
        DOMTree = xml.dom.minidom.parse(self.apiSpecXml)
        De = DOMTree.documentElement
        self.AssertAttr (De, "version")     

        xmlLibs = De.getElementsByTagName("library")
        for xmlLib in xmlLibs:
    
            self.AssertAttr (xmlLib, "name")
            libName = xmlLib.getAttribute("name")
            print ("# Parse library: %s" %libName)
            curLib = PyLib (libName)

            xmlModules = xmlLib.getElementsByTagName ("module")
            for xmlMd in xmlModules:
            
                self.AssertAttr (xmlMd, "name")
                mdName = xmlMd.getAttribute("name")
                curMod = self.ParseMod (mdName, xmlMd)
                curLib.Modules [mdName] = curMod

            # exception under library
            xmlExceps = xmlLib.getElementsByTagName ("errors")
            self.ParseExceps (curLib, xmlExceps)
                
               

      