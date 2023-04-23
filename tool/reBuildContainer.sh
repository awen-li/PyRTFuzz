
#docker stop $(docker ps -a -f "name=pyrtfuzz")
#docker rm $(docker ps -a -f "name=pyrtfuzz")

########################################################################
#  40-64: 25 CPUs
########################################################################
image=$1
rq=$2
if [ ! -n "$rq" ]; then
rq="all"
fi

###########
# RQ1
###########
if [ "$rq" == "rq1" ] || [ "$rq" == "all" ]; then
# 1.1 for bug finding: 15 CPUs
./autofuzz.sh run $image python3.9 59 5
./autofuzz.sh run $image python3.8 54 5
./autofuzz.sh run $image python3.7 49 5

# 1.2 for coverage/appnum report 1 CPU
./autofuzz.sh run $image python3.9 48 1 covapp
fi

###########
# RQ2
###########
if [ "$rq" == "rq2.1" ] || [ "$rq" == "rq2" ] || [ "$rq" == "all" ]; then
# 2.1 Untyped <-> Typed (Dynamic data type extraction)
./autofuzz.sh run $image python3.9 46 2 typed
fi

# 2.2 (Level-2) Fuzzing budget: 10 -> 30 -> 60 -> 90 -> 180 -> 360
if [ "$rq" == "rq2.3" ] || [ "$rq" == "rq2" ] || [ "$rq" == "all" ]; then
./autofuzz.sh run $image python3.9 40 6 budget
fi


if [ "$rq" == "rq2.2" ] || [ "$rq" == "rq2" ] || [ "$rq" == "all" ]; then
# 2.3 (Level-1) for complexity: 1 -> 4 -> 16 -> 64 -> 128 -> 256 -> 512 -> 1024 (Built-in commands)
./autofuzz.sh run $image python3.9 1 8 complex
fi

