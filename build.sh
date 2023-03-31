
BASE_DIR=`pwd`
INSTALL_PATH=/root/anaconda3
PRIMARY_PYTHON=python3.9
ALL_VERSIONS=("3.9.15" "3.8.15" "3.7.15")

setPython ()
{
	py=$1
	cd $INSTALL_PATH/bin
	if [ -L "python" ]; then
		unlink python
	fi

	ln -s $py python
	cd -
	
	echo "### setPython -> $py"
	export PYTHON_LIBRARY=$INSTALL_PATH/lib/$PRIMARY_PYTHON
}

Action=$1
if [ ! -n "$Action" ]; then
	Action="all"
fi


# 1. build libfuzzer
if [ "$Action" == "llvm" ] || [ "$Action" == "all" ]; then
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
fi


if [ "$Action" == "python" ] || [ "$Action" == "all" ]; then
	for Ver in ${ALL_VERSIONS[@]}
	do
		setPython $PRIMARY_PYTHON
		python --version

		INSTALL_VER=`echo ${Ver: 0: 3}`
		echo "### Start to compile python$INSTALL_VER"

		# 2. install python from source
		cd $BASE_DIR/cpython
		PYTHON_PATH="Python-$Ver"
		if [ ! -d "$PYTHON_PATH" ]; then
			apt-get install openssl	
			tar -xvf $PYTHON_PATH.tar.xz
			
			cd $PYTHON_PATH && ./configure --prefix=$INSTALL_PATH --enable-optimizations --with-openssl=/root/anaconda3
			make clean && make && make altinstall
		fi
		rm -rf $PYTHON_PATH

		# 3. build atheris
		setPython "python$INSTALL_VER"
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
	done
fi
