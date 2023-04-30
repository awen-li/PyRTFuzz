FUZZRES="../FuzzResult"

if [ ! -d "$FUZZRES" ]; then
	echo "No Fuzz$FUZZRESResult exists!"
	exit 0
fi

# RQ1 - Cov & AppNum
cp -rf $FUZZRES/GPU-cailab-FuzzResult-*-covapp RQ1/ 
python picDraw.py -q rq1

# RQ2 - PyGen
python picDraw.py -q rq2


# RQ3.1 - complexity <---> Cov & AppNum
cp -rf $FUZZRES/GPU-cailab-FuzzResult-*-complex* RQ3.1/ 
python picDraw.py -q rq3.1



# RQ3.2 - Lv2Budget <---> Cov & AppNum
cp -rf $FUZZRES/GPU-cailab-FuzzResult-*-Budget* RQ3.2/ 
python picDraw.py -q rq3.2


# RQ3.2 - Typed/UnTyped <---> Cov & AppNum
cp -rf $FUZZRES/GPU-cailab-FuzzResult-*typed RQ3.3/ 
python picDraw.py -q rq3.3

