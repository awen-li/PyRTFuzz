
BASE_DIR=`pwd`

STC_SPEC=$BASE_DIR/StcSpec
DYN_SPEC=$BASE_DIR/DynSpec

CPYTHON_PATH=`cd ../../cpython/Python-3.9.15/Lib && pwd`
echo $CPYTHON_PATH
TIMIE_LIMIT=600

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
			pyId=`ps -ef | grep $process | grep -v grep | awk '{print $2}'`
			echo "### $process[$pyId] runs over $TIMIE_LIMIT, force it to exit now........"
			
			kill -9 $pyId
			break
		fi	
	done
	sleep 1
}

# 1. generate basic spec through static analysis
if [ ! -f "apispec.xml" ]; then
	python -m specgen $CPYTHON_PATH
	if [ ! -f "apispec.xml" ]; then
		echo "@@@ Generate apispec.xml fail........."
		exit 0
	fi
fi


# 2. update data types through dynamic tracing
CPYTHON_TESTS=$CPYTHON_PATH/test

INDEX=1
CHACHE_FILES="cache.tmp"
touch $CHACHE_FILES
ALL_TESTS=`find $CPYTHON_TESTS -name "test*py"`
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
        
    EndTime=`date '+%s'`
    TimeCost=`expr $EndTime - $StartTime`
    echo "[$test]@@@@@ time cost: $TimeCost [$StartTime, $EndTime]"
    
    let INDEX=$INDEX+1
    echo $test >> $CHACHE_FILES
done

# 3. update api expr
python -m specgen -e apispec.xml

# 4. output the statistic
python -m specgen -c apispec.xml