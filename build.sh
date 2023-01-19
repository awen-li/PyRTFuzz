
BASE_DIR=`pwd`
INSTALL_PATH=/root/anaconda3
PRIMARY_PYTHON=python3.9

setPython ()
{
	py=$1
	cd $INSTALL_PATH/bin
	if [ -L "python" ]; then
		unlink python
	fi

	ln -s $py python
	cd -
	
	export PYTHON_LIBRARY=$INSTALL_PATH/lib/$PRIMARY_PYTHON
}


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


# 2. install python from source
cd $BASE_DIR/cpython
setPython $PRIMARY_PYTHON
python --version

PYTHON_VER=Python-3.9.15
if [ ! -d "$PYTHON_VER" ]; then
	apt-get install openssl	
	tar -xvf $PYTHON_VER.tar.xz
	
	cd $PYTHON_VER && ./configure --prefix=$INSTALL_PATH --enable-optimizations --with-openssl=/root/anaconda3
	make clean && make && make altinstall
fi

# 3. build atheris
setPython python3.9
export ASAN_OPTIONS=detect_leaks=0
cd $BASE_DIR/atheris
if [ -d "build" ]; then
	rm -rf build
fi
python setup.py install
cd -


# 4. install fuzzwrapper
cd $BASE_DIR/fuzzwrapper && ./build.sh && cd -



# 5. install apispec toolkit
cd $BASE_DIR/apispec && ./build.sh && cd -
