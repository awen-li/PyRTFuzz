function setPython ()
{
	cd $INSTALL_PATH/bin

	py=$1
	if [ -L "python" ]; then
		unlink python
	fi
	ln -s $py python
	echo "### set Python -> $py"

	if [ -L "pip" ]; then
		unlink pip
	fi
	Pip=`echo ${py/python/pip}`
	ln -s $Pip pip
	echo "### set Pip -> $Pip"

	export PYTHON_LIBRARY=$INSTALL_PATH/lib/$PRIMARY_PYTHON
	cd -
}

setPython $1