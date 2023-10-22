
export PY_PATH=`pwd`

if [ ! -f "apispec.xml" ]; then
	ln -s ../PySpec/CPY_3.9.15_apispec.xml apispec.xml
fi
export PYRTF_CODEGEN_TIME=1
touch evaluate.log

apt-get install cloc

# complexity 
Complexity=(1 4 16 64 128 256 512 1024 2048 4096)
for Compl in ${Complexity[@]}
do
	export PYRTF_COMPLEXITY=$Compl
	echo "Set PYRTF_COMPLEXITY=$Compl"
	echo "Set PYRTF_COMPLEXITY=$Compl" >> evaluate.log

	echo "python -m appgen -g -a sqlite3.dbapi2.DateFromTicks apispec.xml"
	python -m appgen -g -a sqlite3.dbapi2.DateFromTicks apispec.xml >> evaluate.log

	cloc sqlite3#dbapi2#DateFromTicks.py
	cloc sqlite3#dbapi2#DateFromTicks.py >> evaluate.log

	echo >> evaluate.log
	echo >> evaluate.log
	echo
	echo
done
