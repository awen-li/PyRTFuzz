# CpyFuzz
fuzzing on python interpreter

Useable docker image for CpyFuzz: ```docker pull daybreak2019/cpyfuzz:v1.0 ```

```
CpyFuzz
+-- atheris          --------------    the python fuzzer
+-- cpython          --------------    the cpython package for testing
+-- documents        --------------    the design documents for CpyFuzz
+-- experiments      --------------    the data and scripts for experiments
+-- fuzzwrapper      --------------    a wrapper for level-2 fuzzing
+-- libfuzzer        --------------    the fuzzing core (for both python and c)
+-- tool             --------------    some self-developed tools for CpyFuzz
+-- build.sh         --------------    the build script for CpyFuzz

```
