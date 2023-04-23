from fuzzwrap import PyDecode 
from html.parser import *
import html
import html.parser
from html import unescape

CLS_TYPE_LIST = []
API_TYPE_LIST = ['str']

def demoFunc(arg):
    try:
        obj = html.parser.HTMLParser()
        data = PyDecode(API_TYPE_LIST, arg)
        obj.feed(data)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        demoFunc(x)
