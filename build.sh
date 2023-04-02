
BASE_DIR=`pwd`
INSTALL_PATH=/root/anaconda3
PRIMARY_PYTHON=python3.9
ALL_VERSIONS=("3.9.15" "3.8.15" "3.7.15")

Action=$1
if [ ! -n "$Action" ]; then
	Action="all"
fi


# build libfuzzer
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

cp $BASE_DIR/tool/setPython.sh /usr/bin
setPython.sh $PRIMARY_PYTHON
if [ "$Action" == "python" ] || [ "$Action" == "all" ]; then
	for Ver in ${ALL_VERSIONS[@]}
	do
		echo "### Start to compile python$Ver"

		# install python from source
		cd $BASE_DIR/cpython
		PYTHON_PATH="Python-$Ver"
		if [ ! -d "$PYTHON_PATH" ]; then
			apt-get install openssl	
			tar -xvf $PYTHON_PATH.tar.xz
		fi

		cd $PYTHON_PATH && ./configure --prefix=$INSTALL_PATH --enable-optimizations --with-openssl=/root/anaconda3
		make clean && make && make altinstall
		rm -rf $PYTHON_PATH

		cd $BASE_DIR
	done
fi


if [ "$Action" == "prtfuzz" ] || [ "$Action" == "all" ]; then
	for Ver in ${ALL_VERSIONS[@]}
	do
		INSTALL_VER=`echo ${Ver: 0: 3}`
		setPython.sh "python$INSTALL_VER"

		# build atheris	
		export ASAN_OPTIONS=detect_leaks=0
		cd $BASE_DIR/atheris
		if [ -d "build" ]; then
			rm -rf build
		fi
		python setup.py install
		cd -

		# install fuzzwrapper
		cd $BASE_DIR/fuzzwrapper && ./build.sh && cd -


		# install apispec toolkit
		cd $BASE_DIR/apispec && ./build.sh && cd -
	done
fi

setPython.sh $PRIMARY_PYTHON
