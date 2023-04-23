from fuzzwrap import PyDecode 
from xml.sax.xmlreader import *
import xml
import xml.sax
import xml.sax.xmlreader
from xml.sax import handler
from xml.sax import saxutils

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['None']

def demoFunc(arg):
    try:
        obj = xml.sax.xmlreader.IncrementalParser()
        source = PyDecode(API_TYPE_LIST, arg)
        obj.parse(source)
    except (AssertionError, AttributeError, KeyError, LookupError, NotImplementedError, OSError, SAXNotRecognizedException, SAXNotSupportedException, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    PyCall_1681356749_UdCYM(x)

def PyCall_1681356749_UdCYM(x):
    demoFunc(x)
