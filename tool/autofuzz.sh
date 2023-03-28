#!/bin/bash

MinCpu=0
MaxCpu=9

Action=$1
Image=""

function RunFuzzer ()
{
	ID=$MinCpu
	while [ $ID -le $MaxCpu ]
	do
   		FuzzName="cpyfuzz-inst-$ID"
		docker run -itd --name "$FuzzName" $Image
		docker exec -itd $FuzzName bash "cd /root/CpyFuzz/experiments; python -m fuzzloop -pyscript=seeds -cpu=$ID"
		let Inst++
	done	
}

function DelFuzzer ()
{
	ID=$MinCpu
	while [ $ID -le $MaxCpu ]
	do
   		FuzzName="cpyfuzz-inst-$ID"
		Dck=`docker ps  | grep $FuzzName`
		if [ ! -n "$Dck" ]; then
			continue
		fi
		docker stop $FuzzName
		docker rm $FuzzName
		let Inst++
	done	
}


function Collect ()
{
	ID=$MinCpu
	while [ $ID -le $MaxCpu ]
	do
   		FuzzName="cpyfuzz-inst-$ID"
		Dck=`docker ps  | grep $FuzzName`
		if [ ! -n "$Dck" ]; then
			echo "$FuzzName does not exist!!!"
			continue
		fi

		docker exec -it $FuzzName bash "cd /root/CpyFuzz/experiments; python -m pycollect"

		LocalDir="$HOSTNAME-FuzzResult-$FuzzName"
		if [ ! -d "$LocalDir" ]; then
			mkdir $LocalDir
		fi
		docker cp $FuzzName:/root/CpyFuzz/experiments/FuzzResult $LocalDir

		let Inst++
	done	
}


if [ "$Action" == "run" ]; then
	Image=$2
	if [ ! -n "$Image" ]; then
		echo "Please specify the Iage"
		exit
	fi
	RunFuzzer

elif [ "$Action" == "collect" ]; then
	Collect

elif [ "$Action" == "del" ]; then
	DelFuzzer
	
else:
	echo "### Not support the action input: [run / collect / del]"

