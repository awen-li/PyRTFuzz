
export PYTRACE_PATH=`pwd`

echo ""
echo ""
echo "@@@@@@@@@@@@@@@ build Python:spectrace @@@@@@@@@@@@@@@"
pip install .

PyVersion=`python -c 'import platform; major, minor, patch = platform.python_version_tuple(); print(str(major)+"."+str(minor))'`

# anaconda environment
Anaconda=`which anaconda`
if [ -n "$Anaconda" ]; then   
    PYTHON_PATH=/root/anaconda3/lib/python$PyVersion
    if [ -d "$PYTHON_PATH" ]; then
    	cp $PYTRACE_PATH/spectrace.py $PYTHON_PATH
    	echo "Have installed pygen to anaconda...."

        # clone customized unittest
        if [ ! -d "unittest-PRT" ]; then
            git clone https://github.com/Daybreak2019/unittest-PRT.git
        fi
        UT=$PYTRACE_PATH/unittest-PRT/unittest_python$PyVersion
        echo "### Currrent customized unittest is: $UT, try to link as $PYTHON_PATH/unittest"

        if [ -d "$PYTHON_PATH/unittest" ]; then
            mv $PYTHON_PATH/unittest $PYTHON_PATH/unittest_back
        elif [ -L "$PYTHON_PATH/unittest" ]; then
            unlink $PYTHON_PATH/unittest
        elif [ -f "$PYTHON_PATH/unittest" ]; then
            rm -f $PYTHON_PATH/unittest
        fi

        cd $PYTHON_PATH && ln -s $UT unittest && cd -
    fi
fi

