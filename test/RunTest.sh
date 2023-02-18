
BASE_DIR=`pwd`

let INDEX=1
ALL_TESTS=`find ./ -name "pyfuzz*py"`
for test in $ALL_TESTS
do
    echo
    echo
    echo "[$INDEX]********************* Running ---- <$test> ---- *********************"
    python $test
    
    let INDEX=$INDEX+1
done
