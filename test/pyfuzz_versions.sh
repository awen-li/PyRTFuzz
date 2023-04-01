
ALL_VERSIONS=("3.9.15" "3.8.15" "3.7.15")

for Ver in ${ALL_VERSIONS[@]}
do
    INSTALL_VER=`echo ${Ver: 0: 3}`
    setPython.sh "python$INSTALL_VER"

    if [ "$?" == 0 ]; then
        python -m appgen -s 
    fi
 
done