
BASE_DIR=`pwd`

# 1. build libfuzzer
if [ ! -n "$LLVM_PATH" ]; then
	echo "Plase set LLVM_PATH before building libfuzzer!"
	exit 0
fi

cd $LLVM_PATH/llvm-11.0.0.src/projects/compiler-rt-11.0.0.src/lib/
if [ ! -L fuzzer ]; then
	if [ -d fuzzer ]; then
		rm -rf fuzzer
	fi
	
	ln -s $BASE_DIR/libfuzzer fuzzer
fi

cd $LLVM_PATH/build
make -j4


# 2. build atheris
cd $BASE_DIR/atheris
if [ -d "build" ]; then
	rm -rf build
fi
python setup.py install


# 3. install fuzzwrapper
cd fuzzwrapper && ./build.sh && cd -