# CpyFuzz
fuzzing on python interpreter

Useable docker image for CpyFuzz: ```docker pull daybreak2019/cpyfuzz:v2.0 ```
Use the ``` . build.sh ``` to build the whole program.

```
CpyFuzz
+-- apispec          --------------    API spec collection
+-- atheris          --------------    the python fuzzer
+-- cpython          --------------    the cpython package for testing
+-- documents        --------------    the design documents for CpyFuzz
+-- experiments      --------------    the data and scripts for experiments
+-- fuzzwrapper      --------------    a wrapper for level-2 fuzzing
+-- libfuzzer        --------------    the fuzzing core (for both python and c)
+-- tool             --------------    some self-developed tools for CpyFuzz
+-- build.sh         --------------    the build script for CpyFuzz

```

## Install Cpython-3.9 with instrumentation
```
cd CpyFuzz/experiments && ./buildCPython.sh 
```

## Collect API specs from cpython runtimes
```
cd CpyFuzz/apispec/PySpec && ./genSpec.sh
```

## Run the basic test cases
```
cd CpyFuzz/test && ./RunTest.sh
```


## Run the fuzzing on cpython&runtimes
```
# run the fuzzing in loop with docker image: daybreak2019/cpyfuzz:v2.0
cd CpyFuzz/experiments
python -m fuzzloop -pyscript=seeds &

# collect fuzzing results
cd CpyFuzz/experiments
python -m pycollect
```

## Example for python APP generation
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
