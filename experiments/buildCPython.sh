
BASE_DIR=`pwd`
INSTALL_PATH=/root/anaconda3
PYTHON_VER=Python-3.9.15

setPython ()
{
	py=$1
	cd $INSTALL_PATH/bin
	if [ -L "python" ]; then
		unlink python
	fi

	ln -s $py python
	cd -
}

setPython python3.9
export ASAN_OPTIONS=detect_leaks=0

LD_CLANG="$(python -c "import sysconfig; print(sysconfig.get_config_var('LDSHARED'))")"	
LD_CLANG=`echo $LD_CLANG | sed 's/^gcc/clang/'`

export LDFLAGS="$(python -c "import atheris; print(atheris.path())")/asan_with_fuzzer.so -pthread"
export LDSHARED=$LD_CLANG
export CC="clang" CFLAGS="-fsanitize=fuzzer-no-link" CXX="clang++" CXXFLAGS="-fsanitize=fuzzer-no-link"

if [ ! -d "$PYTHON_VER" ]; then
	cp ../cpython/$PYTHON_VER.tar.xz ./
	tar -xvf $PYTHON_VER.tar.xz
	cd $PYTHON_VER && ./configure --prefix=$INSTALL_PATH --enable-optimizations --with-openssl=/root/anaconda3
	
	make clean && make
	make altinstall
	cd -

	#link to the current python
	setPython python3.9	
fi




