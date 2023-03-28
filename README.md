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
