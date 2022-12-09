
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

class ApiSpec():
    def __init__(self, apiSpecXml='apispec.xml'):
        self.apiSpecXml = apiSpecXml


    def AssertAttr (self, node, attr):
        if not node.hasAttribute(attr):
            print ("Node item has no attribute %s!" %attr)
            exit (0)

    def ParseApi (self, ApiNode):
        pass

    def ParseExceps (self, ExcepNode):
        pass

    def ParseClass (self, ClsNode):
        pass
        
    def Parser (self):
        DOMTree = xml.dom.minidom.parse(self.apiSpecXml)
        De = DOMTree.documentElement
        if De.hasAttribute("version"):
           print ("API spec version: %s" % De.getAttribute("shelf"))
         

        libraries = De.getElementsByTagName("library")
        for lib in libraries:
    
            self.AssertAttr (lib, "name")
            libName = lib.getAttribute("name")
            print ("# Parse library: %s" %libName)

            modules = lib.getElementsByTagName ("module")
            for md in modules:
            
                self.AssertAttr (md, "name")
                mdName = md.getAttribute("name")
                print ("\t# Parse module: %s" %mdName)

                # class under modules
                classes = md.getElementsByTagName ("class")
                for cls in classes:
                
                    self.AssertAttr (cls, "name")
                    clsName = cls.getAttribute("name")
                    print ("\t\t# Parse class: %s" %clsName)
                    self.ParseClass (cls)

                # exception under modules
                exceps = md.getElementsByTagName ("errors")
                self.ParseExceps (exceps)

                # api under module
                apis = md.getElementsByTagName ("api")
                for api in apis:
                    self.ParseApi (api)
               

      