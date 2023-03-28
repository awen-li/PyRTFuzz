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
		echo "\n Start Fuzzer $FuzzName..."
		docker run -itd --name "$FuzzName" $Image
		docker exec -itd -w /root/CpyFuzz/experiments $FuzzName bash autorun.sh run $ID
		let ID++
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
			let ID++
			continue
		fi
		docker stop $FuzzName
		docker rm $FuzzName
		let ID++
	done	
}


function Collect ()
{
	ID=$MinCpu
	while [ $ID -le $MaxCpu ]
	do
   		FuzzName="cpyfuzz-inst-$ID"
		Dck=`docker ps | grep $FuzzName`
		if [ ! -n "$Dck" ]; then
			echo "$FuzzName does not exist!!!"
			let ID++
			continue
		fi

		echo "\n Collecting experiment results from $FuzzName..."
		docker exec -itd -w /root/CpyFuzz/experiments $FuzzName bash autorun.sh collect

		LocalDir="$HOSTNAME-FuzzResult-$FuzzName"
		if [ ! -d "$LocalDir" ]; then
			mkdir $LocalDir
		fi
		docker cp $FuzzName:/root/CpyFuzz/experiments/FuzzResult $LocalDir

		let ID++
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

else
	echo "### Not support the action input: [run / collect / del]"
fi
