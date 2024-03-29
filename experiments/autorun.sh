export CONDA_EXE=/root/anaconda3/bin/conda
export CONDA_PREFIX=/root/anaconda3
export ASAN_OPTIONS=detect_leaks=0
export HOME=/root
export CONDA_PYTHON_EXE=/root/anaconda3/bin/python
export CONDA_PROMPT_MODIFIER=(base) 
export LLVM_PATH=/root/tools/llvm11
export PATH=/root/anaconda3/bin:/root/anaconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/root/tools/llvm11/build/bin
export CLANG_PATH=/root/tools/llvm11/build/bin
export CONDA_DEFAULT_ENV=base

function setPyEnv ()
{
    PY=$1
    setPython.sh $PY

    # link apispec here
    SpecFile=`python -c "from pyspec import ApiSpecGen; print(ApiSpecGen.GetSpecName())"`
    if [ -L "apispec.xml" ]; then
        unlink apispec.xml
    fi
    ln -s ../apispec/PySpec/$SpecFile apispec.xml
}

ACTION=$1
if [ "$ACTION" == "run" ]; then

    CPUID=$2
    if [ ! -n "$CPUID" ]; then
        echo "please specify CPUID!"
    fi

    PY=$3
    if [ ! -n "$PY" ]; then
        PY=python3.9
    fi

    SubAct=$4

    setPyEnv $PY

    if [ -n "$SubAct" ]; then
        python -m fuzzloop -history -pyscript=seeds_$PY -cpu=$CPUID -$SubAct
    else
        python -m fuzzloop -pyscript=seeds_$PY -cpu=$CPUID
    fi

elif [ "$ACTION" == "collect" ]; then

    PY=$2
    if [ ! -n "$PY" ]; then
        PY=python3.9
    fi
    setPyEnv $PY

    python -m pycollect seeds_$PY

else
    echo "Not support the command [run / collect]"
fi




