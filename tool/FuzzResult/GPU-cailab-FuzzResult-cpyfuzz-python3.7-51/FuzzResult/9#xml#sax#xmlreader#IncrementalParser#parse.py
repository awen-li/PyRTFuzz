from fuzzwrap import PyDecode 
from xml.sax.xmlreader import *
import xml
import xml.sax
import xml.sax.xmlreader
from xml.sax import handler
from xml.sax import saxutils

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = xml.sax.xmlreader.IncrementalParser()
            source = PyDecode(API_TYPE_LIST, arg)
            obj.parse(source)
            PyPrint(obj)
            repr(obj)
        except (AssertionError, AttributeError, KeyError, LookupError, NotImplementedError, OSError, SAXNotRecognizedException, SAXNotSupportedException, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        if True:
            with open('/dev/null', 'r'):
                if True:
                    if True:
                        dc = demoCls()
                        dc.demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
