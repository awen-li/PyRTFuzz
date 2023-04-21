#!/bin/bash

MinCpu=0
MaxCpu=9

Action=$1
Image=""
PyVersion=python3.9
ALL_VERSIONS=("python3.9" "python3.8" "python3.7")
GitPush="yes"

SubTask=""

function Help ()
{
	echo
	echo "#########################################################################"
	echo "### autofuzz.sh run [docker-image] [python-version] [start-cpu] [cpu-num]"
	echo "### autofuzz.sh collect [GitPush:yes (default) / no]"
	echo "### autofuzz.sh del"
	echo "#########################################################################"
	echo
}

function RunFuzzer_BugF ()
{
	ID=$MinCpu
	while [ $ID -lt $MaxCpu ]
	do
   		FuzzName="cpyfuzz-$PyVersion-$ID"
		echo
		echo "### Start Fuzzer $FuzzName..."
		docker run -itd --name "$FuzzName" $Image
		if [ $((ID % 2)) -eq 0 ]; then
			docker exec -itd -w /root/CpyFuzz/experiments $FuzzName bash autorun.sh run $ID $PyVersion
		else
			docker exec -itd -w /root/CpyFuzz/experiments $FuzzName bash autorun.sh run $ID $PyVersion "lv2budget=30"
		fi
		let ID++
	done
}

function DelFuzzer ()
{
	ID=$MinCpu
	while [ $ID -lt $MaxCpu ]
	do
   		FuzzName="cpyfuzz-$PyVersion-$ID"
		Dck=`docker ps  | grep $FuzzName | awk '{print $10}'`
		if [ ! -n "$Dck" ]; then
			let ID++
			continue
		fi
		docker stop $Dck
		docker rm $Dck
		let ID++
	done	
}

function GetFuzzerName ()
{
	Fuzzer=$1
	Containers=`docker ps --format "{{.Names}}"`
	for Con in $Containers
	do
		isFuzzer=`echo $Con | grep $Fuzzer`
		if [ ! -n "$isFuzzer" ]; then
		    continue
		fi

		echo $Con
		return
	done

	return
}


function Collect ()
{
	if [ "$GitPush" == "yes" ]; then
		git clone git@github.com:yhryyq/FuzzResult.git
	else
		if [ ! -d "FuzzResult" ]; then
			mkdir FuzzResult
		fi
	fi

	ID=$MinCpu
	while [ $ID -lt $MaxCpu ]
	do
		FuzzName=`GetFuzzerName cpyfuzz-$PyVersion-$ID-`
		if [ ! -n "$FuzzName" ]; then
		    FuzzName=`GetFuzzerName cpyfuzz-$PyVersion-$ID`
			if [ ! -n "$FuzzName" ]; then
				let ID++
				continue
			fi	
		fi

		echo
		echo "### Collecting experiment results from $FuzzName..."
		docker exec -it -w /root/CpyFuzz/experiments $FuzzName bash autorun.sh collect $PyVersion
	
		LocalDir="$HOSTNAME-FuzzResult-$FuzzName"
		if [ ! -d "FuzzResult/$LocalDir" ]; then
			mkdir FuzzResult/$LocalDir
		fi
		docker cp $FuzzName:/root/CpyFuzz/experiments/FuzzResult/ FuzzResult/$LocalDir

		let ID++
	done

	if [ "$GitPush" == "yes" ]; then
		cd FuzzResult
		git add .
		git commit -m "server-192 $(date +%Y-%m-%d" "%H:%M:%S)"
		git push
		cd ..
		rm -rf FuzzResult
	fi
}

if [ "$Action" == "help" ]; then
	Help
elif [ "$Action" == "run" ]; then
	Image=$2
	if [ ! -n "$Image" ]; then
		echo "Please specify the Iage"
		docker image ls | grep cpyfuzz
		exit
	fi

	PyVersion=$3
	if [ ! -n "$PyVersion" ]; then
		echo "Please specify the python version for fuzzing:"
		for Ver in ${ALL_VERSIONS[@]}
		do
			echo "                $Ver"
		done
		exit
	fi

	if [ -n "$4" ]; then
		MinCpu=$4
	fi

	if [ -n "$5" ]; then
		MaxCpu=`expr $MinCpu + $5`
	fi

	SubTask=$6

	echo "### Run the fuzzers on CPU [$MinCpu: `expr $MaxCpu-1`]..."
	if [ ! -n "$SubTask" ]; then
		RunFuzzer_BugF

	elif [ "$SubTask" == "covapp" ]; then
		FuzzName="cpyfuzz-$PyVersion-$MinCpu-covapp"
		docker run -itd --name "$FuzzName" $Image
		docker exec -itd -w /root/CpyFuzz/experiments $FuzzName bash autorun.sh run $MinCpu $PyVersion "maskexcp"

	elif [ "$SubTask" == "typed" ]; then
		# typed
		FuzzName="cpyfuzz-$PyVersion-$MinCpu-typed"
		docker run -itd --name "$FuzzName" $Image
		docker exec -itd -w /root/CpyFuzz/experiments $FuzzName bash autorun.sh run $MinCpu $PyVersion "typed"
		let MinCpu++

		# untyped
		FuzzName="cpyfuzz-$PyVersion-$MinCpu-untyped"
		docker run -itd --name "$FuzzName" $Image
		docker exec -itd -w /root/CpyFuzz/experiments $FuzzName bash autorun.sh run $MinCpu $PyVersion "untyped"

	elif [ "$SubTask" == "complex" ]; then
		Complex=(1 4 16 64 128 256 512 1024)
		CPUID=$MinCpu
		for Compl in ${Complex[@]}
		do
			FuzzName="cpyfuzz-$PyVersion-$CPUID-$SubTask-$Compl"
			docker run -itd --name "$FuzzName" $Image
			if [ $Compl == 1024 ]; then
				docker exec -itd -w /root/CpyFuzz/experiments $FuzzName bash autorun.sh run $CPUID $PyVersion "complex=$Compl -timeout=600"
			else
				docker exec -itd -w /root/CpyFuzz/experiments $FuzzName bash autorun.sh run $CPUID $PyVersion "complex=$Compl"
			fi
			let CPUID++
		done 

	elif [ "$SubTask" == "budget" ]; then
		Budgets=(1 30 60 90 180 360)
		CPUID=$MinCpu
		for Bgt in ${Budgets[@]}
		do
			FuzzName="cpyfuzz-$PyVersion-$CPUID-Budget-$Bgt"
			docker run -itd --name "$FuzzName" $Image
			docker exec -itd -w /root/CpyFuzz/experiments $FuzzName bash autorun.sh run $CPUID $PyVersion "lv2budget=$Bgt -maskexcp"
			let CPUID++
		done
	fi

elif [ "$Action" == "collect" ]; then

	GitPush=$2
	if [ ! -n "$GitPush" ]; then
		GitPush="yes"
	fi
	
	for Ver in ${ALL_VERSIONS[@]}
	do
		MinCpu=0
		MaxCpu=`nproc --all`
		PyVersion=$Ver
		Collect
	done

elif [ "$Action" == "del" ]; then

	for Ver in ${ALL_VERSIONS[@]}
	do
		MinCpu=0
		MaxCpu=`nproc --all`
		PyVersion=$Ver
		DelFuzzer
	done

else
	echo "### Not support the action input: $Action"
	Help
fi
