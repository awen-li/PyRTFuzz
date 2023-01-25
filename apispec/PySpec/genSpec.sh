
BASE_DIR=`pwd`

STC_SPEC=$BASE_DIR/StcSpec
DYN_SPEC=$BASE_DIR/DynSpec

CPYTHON_PATH=`cd ../../cpython/Python-3.9.15/Lib && pwd`
echo $CPYTHON_PATH

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

ALL_TESTS=`find $CPYTHON_TESTS -name "test*py"`
for test in $ALL_TESTS
do
    StartTime=`date '+%s'`
        
    echo
    echo
    echo "********************* Tracing the script ---- <$test> ---- *********************"
    python -m spectrace $test
        
    EndTime=`date '+%s'`
    TimeCost=`expr $EndTime - $StartTime`
    echo "[$test]@@@@@ time cost: $TimeCost [$StartTime, $EndTime]"
done