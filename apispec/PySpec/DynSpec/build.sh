
export PY_PATH=`pwd`

echo ""
echo ""
echo "@@@@@@@@@@@@@@@ build Python:spectrace @@@@@@@@@@@@@@@"
pip install .
cd -

PyVersion=`python -c 'import platform; major, minor, patch = platform.python_version_tuple(); print(str(major)+"."+str(minor))'`

# anaconda environment
Anaconda=`which anaconda`
if [ -n "$Anaconda" ]; then   
    PYTHON_PATH=/root/anaconda3/lib/python$PyVersion
    if [ -d "$PYTHON_PATH" ]; then
    	cp $PY_PATH/spectrace.py $PYTHON_PATH
    	echo "Have installed pygen to anaconda...."

        UT=$PWD/unittest
        if [ -d "$PYTHON_PATH/unittest" ]; then
            mv $PYTHON_PATH/unittest $PYTHON_PATH/unittest_back
        elif [ -L "$PYTHON_PATH/unittest" ]; then
            unlink $PYTHON_PATH/unittest
        fi

        cd $PYTHON_PATH && ln -s $UT unittest && cd -
    fi
fi

