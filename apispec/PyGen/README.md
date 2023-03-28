

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
p = For (p)
p = For (p)
p = While (p)
p = While (p)
p = For (p)
p = While (p)
p = For (p)
p = While (p)
p = While (p)
p = While (p)
p = For (p)
p = While (p)
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
    except (AttributeError, OSError, TypeError, ValueError):
        pass

def RunFuzzer(x):
    W_i6 = 0
    while (W_i6 in range(0, 6)):
        for F_W1 in range(0, 1):
            W_c5 = 0
            while (W_c5 in range(0, 5)):
                W_K4 = 0
                while (W_K4 in range(0, 4)):
                    W_C6 = 0
                    while (W_C6 in range(0, 6)):
                        for F_V3 in range(0, 3):
                            W_d2 = 0
                            while (W_d2 in range(0, 2)):
                                for F_D3 in range(0, 3):
                                    W_F3 = 0
                                    while (W_F3 in range(0, 3)):
                                        W_V4 = 0
                                        while (W_V4 in range(0, 4)):
                                            for F_X6 in range(0, 6):
                                                for F_W1 in range(0, 1):
                                                    for F_o2 in range(0, 2):
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
