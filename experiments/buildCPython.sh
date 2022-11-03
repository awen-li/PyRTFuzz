
BASE_DIR=`pwd`

LD_CLANG="$(python -c "import sysconfig; print(sysconfig.get_config_var('LDSHARED'))")"	
LD_CLANG=`echo $LD_CLANG | sed 's/^gcc/clang/'`

export LDFLAGS="$(python -c "import atheris; print(atheris.path())")/asan_with_fuzzer.so"

export LDSHARED=$LD_CLANG
export CC="clang" CFLAGS="-fsanitize=fuzzer-no-link" CXX="clang++" CXXFLAGS="-fsanitize=fuzzer-no-link"


if [ ! -d "cpython" ]; then
	git clone https://github.com/Daybreak2019/cpython.git
	
fi

cd cpython && ./configure
make 
#make install
