
# _*_ coding:utf-8 _*_
import re
from xml.dom.minidom import parse
import xml.dom.minidom

"""
<?xml version="1.0" ?>
<apisepc version="1.0">
    <library name="email">
        <module name="charset">
            <class name="Charset">
                <api>
                        <name>get_body_encoding</name>
                        <expr>ret = get_body_encoding()</expr>
                        <parameters>{}</parameters>
                        <return>{'ret':base64|7bit}</return>
                        <dependences>  </dependences>
                </api>

                <api>
                        <name>header_encode</name>
                        <expr>header_encode(str)</expr>
                        <parameters>{'str':string}</parameters>
                        <return>{}</return>
                        <dependences>  </dependences>
                </api>
            </class>
        </module>

        <module name="contentmanager">
            <api>
                <name>header_encode</name>
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
    def __init__ (self, Cls, ApiName, Expr):
        self.Module  = Module
        self.ApiName = ApiName
        self.Expr    = Expr
        self.Ret     = {}
        self.Parameters = []


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

        
class ApiSpec():
    def __init__(self, apiSpecXml='apispec.xml'):
        self.apiSpecXml = apiSpecXml
        self.PyLib = {}

    def AssertAttr (self, node, attr):
        if not node.hasAttribute(attr):
            print ("Node item has no attribute %s!" %attr)
            exit (0)

    def ParseApi (self, xmlApi):
        pass

    def ParseExceps (self, xmlExp):
        xmlExpList = xmlExp[0].getElementsByTagName("exception")
        for xExp in xmlExpList:
            print (xExp)

    def ParseClass (self, clsName, xmlCls):
        curCls = PyCls (clsName)
        
        xmlApis = xmlCls.getElementsByTagName("api")
        for xmlApi in xmlApis:
            self.ParseApi (xmlApi)

    def ParseMod (self, mdName, xmlMd):
        print ("\t# Parse module: %s" %mdName)
        curMd = PyMod (mdName)

        # class under modules
        xmlClasses = xmlMd.getElementsByTagName ("class")
        print (xmlClasses)
        for xmlCls in xmlClasses:          
            self.AssertAttr (xmlCls, "name")
            clsName = xmlCls.getAttribute("name")
            print ("\t\t# Parse class: %s" %clsName)
                                   
            curCls = self.ParseClass (clsName, xmlCls)

        # api under module
        xmlApis = xmlMd.getElementsByTagName ("api")
        print (xmlApis)
        for xmlApi in xmlApis:
            self.ParseApi (xmlApi)
            
    def Parser (self):
        DOMTree = xml.dom.minidom.parse(self.apiSpecXml)
        De = DOMTree.documentElement
        if De.hasAttribute("version"):
           print ("API spec version: %s" % De.getAttribute("shelf"))
         

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
            self.ParseExceps (xmlExceps)
                
               

      