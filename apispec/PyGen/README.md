

## Gen APP with single API
```
python -m appgen -g -a [api-path] [apispec-path]
```

### Example of generating APP with wingle API
```
python -m appgen -g -a sqlite3.dbapi2.DateFromTicks apispec.xml
```

```
# SL script
p = PO (sqlite3.dbapi2.DateFromTicks)
p = For (p)
p = Repr (p)
p = While (p)
p = While (p)
p = Wtih (p)
p = Repr (p)
p = While (p)
p = Call (p)
```

```
# Python script
from fuzzwrap import PyDecode 
from sqlite3.dbapi2 import *
import sqlite3
import sqlite3.dbapi2

API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        ticks = PyDecode(API_TYPE_LIST, arg)
        ret = sqlite3.dbapi2.DateFromTicks(ticks)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    PyCall_1680969543_NYWjR(x)

def PyCall_1680969543_NYWjR(x):
    W_j2 = 0
    while (W_j2 in range(0, 2)):
        W_j2 += 1
        with open('/dev/null', 'r'):
            W_T3 = 0
            while (W_T3 in range(0, 3)):
                W_T3 += 1
                W_g1 = 0
                while (W_g1 in range(0, 1)):
                    W_g1 += 1
                    for F_v3 in range(0, 3):
                        demoFunc(x)
```



## Example of SL command
### Inherit (email.charset.Charset.get_body_encoding)
```
class demoCls(Charset):

    def __init__(self):
        pass

    def demoFunc1(self, arg1):
        try:
            ret = self.get_body_encoding()
        except (email.errors.MessageError, 
                email.errors.MessageParseError, 
                email.errors.BoundaryError, 
                email.errors.MultipartConversionError):
            pass

    def get_body_encoding():
        sp = super()
        return sp.get_body_encoding()

    def header_encode(str):
        sp = super()
        sp.header_encode(str)

def RunFuzzer(x):
    ob = demoCls()
    ob.demoFunc1(x)
```

### p = OO (email.charset.Charset.get_body_encoding),  p = For (p)
```
class demoCls():

    def __init__(self):
        pass

    def demoFunc1(self, arg1):
        try:
            obj = Charset()
            ret = obj.get_body_encoding()
        except (email.errors.MessageError, 
                email.errors.MessageParseError, 
                email.errors.BoundaryError, 
                email.errors.MultipartConversionError):
            pass

def RunFuzzer(x):
    for M6 in range(0, 6):
        dc = demoCls()
        dc.demoFunc1(x)
```

### p = PO (email.charset.Charset.get_body_encoding),  p = For (p)
```
def demoFunc1(arg1):
    try:
        obj = Charset()
        ret = obj.get_body_encoding()
    except (email.errors.MessageError, 
            email.errors.MessageParseError, 
            email.errors.BoundaryError, 
            email.errors.MultipartConversionError):
        pass

def RunFuzzer(x):
    for j4 in range(0, 4):
        demoFunc1(x)

```
