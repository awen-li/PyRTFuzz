
BASE_DIR=`pwd`
INSTALL_PATH=/root/anaconda3
ALL_VERSIONS=("3.9.15" "3.8.15" "3.7.15")

function InstallPython ()
{
	VERSION=$1
	PYTHON_PATH="Python-"$VERSION
	INSTALL_VER=`echo ${VERSION: 0: 3}`
	
	echo "InstallPython --> $VERSION, $PYTHON_PATH, $INSTALL_VER"
	return

	setPython.sh python$INSTALL_VER
	export ASAN_OPTIONS=detect_leaks=0

	LD_CLANG="$(python -c "import sysconfig; print(sysconfig.get_config_var('LDSHARED'))")"	
	LD_CLANG=`echo $LD_CLANG | sed 's/^gcc/clang/'`

	export LDFLAGS="$(python -c "import atheris; print(atheris.path())")/asan_with_fuzzer.so -pthread"
	export LDSHARED=$LD_CLANG
	export CC="clang" CFLAGS="-fsanitize=fuzzer-no-link" CXX="clang++" CXXFLAGS="-fsanitize=fuzzer-no-link"

	if [ ! -d "$PYTHON_PATH" ]; then
		cp ../cpython/$PYTHON_PATH.tar.xz ./
		tar -xvf $PYTHON_PATH.tar.xz
	fi

	cd $PYTHON_PATH && ./configure --prefix=$INSTALL_PATH --enable-optimizations --with-openssl=/root/anaconda3	
	make clean && make
	make altinstall
	cd -

	rm -rf $PYTHON_PATH/build
}


# Instrument all pythons
for Ver in ${ALL_VERSIONS[@]}
do
	InstallPython $Ver
done

setPython.sh python3.9





