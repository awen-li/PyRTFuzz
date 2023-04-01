
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

PY=$1
if [ "$PY" != "python3.9" ] && [ "$PY" != "python3.8" ] && [ "$PY" != "python3.7" ]; then
    echo "### Support python version [python3.9 / python3.8 / python3.7]"
    exit
fi 

setPyEnv $PY



