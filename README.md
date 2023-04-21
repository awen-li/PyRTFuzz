# PyRTFuzz
fuzzing on python interpreter

Useable docker image for CpyFuzz: ```docker pull daybreak2019/prtfuzz:v1.0 ```
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

## Install Cpython-3.9/3.8/3.7 with instrumentation
```
cd CpyFuzz/experiments && ./buildCPython.sh 
```

## Collect API specs from cpython runtimes
```
cd CpyFuzz/apispec/PySpec
./genSpec.sh python3.9  ----> CPY_3.9.15_apispec.xml
./genSpec.sh python3.8  ----> CPY_3.8.15_apispec.xml
./genSpec.sh python3.7  ----> CPY_3.7.15_apispec.xml
```

## Run the basic test cases
```
cd CpyFuzz/test && ./RunTest.sh
```


## Run the fuzzing on cpython&runtimes
```
PY_VERSIONS=("python3.9" "python3.8" "python3.7")
for Var in ${PY_VERSIONS[@]}

  cd CpyFuzz/experiments
  
  # set python verion and fuzzing environment
  ./setPyEnv.sh $Var
  
  # run the fuzzer 
  python -m fuzzloop -pyscript=seeds_$Var 

  # collect fuzzing results
  cd CpyFuzz/experiments
  python -m pycollect seeds_$Var
  
done
```

## Automatically running the experiments with containers
```
autofuzz.sh run [docker-image] [python3.9/python3.8/python3.7] [start-cpu] [cpu-num]
autofuzz.sh collect [GitPush:yes (default) / no]
autofuzz.sh del
```


## Temporary results:
[FuzzResult](https://github.com/yhryyq/FuzzResult)


