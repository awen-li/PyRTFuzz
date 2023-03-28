export CONDA_EXE=/root/anaconda3/bin/conda
export CONDA_PREFIX=/root/anaconda3
export ASAN_OPTIONS=detect_leaks=0
export PYTHON_LIBRARY=/root/anaconda3/lib/python3.9
export HOME=/root
export CONDA_PYTHON_EXE=/root/anaconda3/bin/python
export CONDA_PROMPT_MODIFIER=(base) 
export LLVM_PATH=/root/tools/llvm11
export PATH=/root/anaconda3/bin:/root/anaconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/root/tools/llvm11/build/bin:/root/PolyFuzz/AFLplusplus
export CLANG_PATH=/root/tools/llvm11/build/bin
export CONDA_DEFAULT_ENV=base

ACTION=$1
if [ "$ACTION" == "run" ]; then

    CPUID=$2
    if [ ! -n "$CPUID" ]; then
        echo "please specify CPUID!"
    fi
    python -m fuzzloop -pyscript=seeds -cpu=$CPUID

elif [ "$ACTION" == "collect" ]; then

    python -m pycollect
    ll FuzzResult

else
    echo "Not support the command [run / collect]"
fi




