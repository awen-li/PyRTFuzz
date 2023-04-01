
BASE_DIR=`pwd`

INSTALL_PATH=/root/anaconda3
STC_SPEC=$BASE_DIR/StcSpec
DYN_SPEC=$BASE_DIR/DynSpec

PY=$1
if [ "$PY" != "python3.9" ] && [ "$PY" != "python3.8" ] && [ "$PY" != "python3.7" ]; then
    echo "### Support python version [python3.9 / python3.8 / python3.7]"
    exit
fi

setPython.sh $PY
export PYTHON_LIBRARY=$INSTALL_PATH/lib/$PY
PythonVersion=`python -c "from platform import python_version; print(python_version())"`

CPYTHON=`cd ../../cpython/ && pwd`
if [ ! -d "$CPYTHON/Python-$PythonVersion" ]; then
	cd $CPYTHON
	tar -xvf Python-$PythonVersion.tar.xz
	cd -
fi

CPYTHON_PATH=$CPYTHON/Python-$PythonVersion/Lib
echo $CPYTHON_PATH
TIMIE_LIMIT=200

Wait ()
{
	second=1
	process=$1
	while true
	do
		count=`ps -ef | grep "$process" | grep -v "grep" | wc -l`
		if [ 0 == $count ];then
			break
		else
			sleep 1
		fi
		
		let second++
		if [ $second == $TIMIE_LIMIT ]; then
			pyId=`ps -ef | grep "$process" | grep -v grep | awk '{print $2}'`
			echo "### $process[$pyId] runs over $TIMIE_LIMIT, force it to exit now........"
			
			kill -9 $pyId
			break
		fi	
	done
	sleep 1
}

# 1. generate basic spec through static analysis
SpecFile=`python -c "from pyspec import ApiSpecGen; print(ApiSpecGen.GetSpecName())"`
if [ ! -f "$SpecFile" ]; then
	python -m specgen $CPYTHON_PATH
	if [ ! -f "$SpecFile" ]; then
		echo "@@@ Generate $SpecFile fail........."
		exit 0
	fi
fi


# 2. update data types through dynamic tracing
CPYTHON_TESTS=$CPYTHON_PATH/test

INDEX=1
CHACHE_FILES="cache.tmp"
touch $CHACHE_FILES
ALL_TESTS=`find $CPYTHON_TESTS -name "test*py"`
FailLog="DynamicTracingFail.txt"
rm -f $FailLog
for test in $ALL_TESTS
do
    StartTime=`date '+%s'`
    
    echo
    echo
    echo "[$INDEX]********************* Tracing the script ---- <$test> ---- *********************"
    IsExist=`cat $CHACHE_FILES | grep $test`
    if [ ! "$IsExist" == "" ]; then
    	let INDEX=$INDEX+1
    	continue
    fi

    python -m spectrace $test &   
    Wait "python -m spectrace"

	if [ ! -f "/tmp/TracingDone" ]; then
		echo "python -m spectrace $test" >> $FailLog
	fi
        
    EndTime=`date '+%s'`
    TimeCost=`expr $EndTime - $StartTime`
    echo "[$test]@@@@@ time cost: $TimeCost [$StartTime, $EndTime]"
    
    let INDEX=$INDEX+1
    echo $test >> $CHACHE_FILES
done

# 3. fast falidate and update api expr
python -m specgen -e $SpecFile
ExprSpecFile=`python -c "from pyspec import ApiSpecGen; print(ApiSpecGen.GetSpecName(\"expr-apispec.xml\"))"`
if [ ! -f "$ExprSpecFile" ]; then
	exit 0
fi
mv $ExprSpecFile $SpecFile

# 4. output the statistic
python -m specgen -c $SpecFile

rm -rf $CPYTHON/Python-$PythonVersion


