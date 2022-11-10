
BASE_DIR=`pwd`
INSTALL_PATH=/root/anaconda3

LD_CLANG="$(python -c "import sysconfig; print(sysconfig.get_config_var('LDSHARED'))")"	
LD_CLANG=`echo $LD_CLANG | sed 's/^gcc/clang/'`

export LDFLAGS="$(python -c "import atheris; print(atheris.path())")/asan_with_fuzzer.so -pthread"

export LDSHARED=$LD_CLANG
export CC="clang" CFLAGS="-fsanitize=fuzzer-no-link" CXX="clang++" CXXFLAGS="-fsanitize=fuzzer-no-link"
export ASAN_OPTIONS=detect_leaks=0

if [ ! -d "cpython" ]; then
	git clone https://github.com/Daybreak2019/cpython.git
	cd cpython && ./configure --prefix=$INSTALL_PATH
	
	cd $BASE_DIR/cpython
	make clean && make
	make install

	#link to the current python
	cd $INSTALL_PATH/bin
	unlink python
	ln -s python3.12 python
fi




