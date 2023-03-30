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
		echo
		echo "### Start Fuzzer $FuzzName..."
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
	git clone git@github.com:yhryyq/FuzzResult.git
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

		echo
		echo "### Collecting experiment results from $FuzzName..."
		docker exec -it -w /root/CpyFuzz/experiments $FuzzName bash autorun.sh collect

		Res=`docker exec -ti -w /root/CpyFuzz/experiments $FuzzName ls FuzzResult`
		IsExist=`echo $Res | grep "cannot access"`
		if [ -n "$IsExist" ]; then
			echo "FuzzResult not found in $FuzzName"
		else
			LocalDir="$HOSTNAME-FuzzResult-$FuzzName"
			if [ ! -d "$LocalDir" ]; then
				mkdir FuzzResult/$LocalDir
			fi
			docker cp $FuzzName:/root/CpyFuzz/experiments/FuzzResult/ FuzzResult/$LocalDir
			 
		fi

		let ID++
	done

	cd FuzzResult
	git add .
	git commit -m "server-192 $(date +%Y-%m-%d" "%H:%M:%S)"
	git push
	cd ..
	rm -rf FuzzResult
}


if [ "$Action" == "run" ]; then
	Image=$2
	if [ ! -n "$Image" ]; then
		echo "Please specify the Iage"
		docker image ls | grep cpyfuzz
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
