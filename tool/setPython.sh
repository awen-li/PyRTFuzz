
INSTALL_PATH=/root/anaconda3

function setPython ()
{
	cd $INSTALL_PATH/bin

	py=$1
	if [ ! -f "$py" ]; then
		echo "### $py is not installed...."
		return 1
	fi

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

	cd -
	return 0
}

setPython $1
exit $?
