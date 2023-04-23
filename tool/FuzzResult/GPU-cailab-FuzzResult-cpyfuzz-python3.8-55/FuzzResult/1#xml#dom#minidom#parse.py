from fuzzwrap import PyDecode 
from xml.dom.minidom import *
import xml
import io
import xml.dom
import xml.dom.minidom
from xml.dom import EMPTY_NAMESPACE
from xml.dom import EMPTY_PREFIX
from xml.dom import XMLNS_NAMESPACE
from xml.dom import domreg
from xml.dom import expatbuilder
from xml.dom import pulldom

API_TYPE_LIST = ['str', 'NoneType', 'NoneType']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (file, parser, bufsize) = PyDecode(API_TYPE_LIST, arg)
            ret = xml.dom.minidom.parse(file, parser, bufsize)
        except (AssertionError, AttributeError, IndexError, KeyError, LookupError, OSError, TypeError, ValueError, xml.dom.HierarchyRequestErr, xml.dom.IndexSizeErr, xml.dom.InuseAttributeErr, xml.dom.InvalidCharacterErr, xml.dom.NamespaceErr, xml.dom.NoModificationAllowedErr, xml.dom.NotFoundErr, xml.dom.NotSupportedErr, xml.dom.WrongDocumentErr) as e:
            pass

def RunFuzzer(x):
    PyCall_1681352783_KXIzl(x)

def PyCall_1681352783_KXIzl(x):
    dc = demoCls()
    dc.demoFunc(x)
