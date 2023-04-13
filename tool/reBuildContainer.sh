
docker stop $(docker ps -a -f "name=cpyfuzz")
docker rm $(docker ps -a -f "name=cpyfuzz")

########################################################################
#  45-64: 20 CPUs
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
./autofuzz.sh run $image python3.9 60 5
./autofuzz.sh run $image python3.8 55 5
./autofuzz.sh run $image python3.7 50 5

# 1.2 for coverage/appnum report 1 CPU
./autofuzz.sh run $image python3.9 49 1 covapp
fi

###########
# RQ2
###########
if [ "$rq" == "rq2.1" ] || [ "$rq" == "rq2" ] || [ "$rq" == "all" ]; then
# 2.1 for Untyped <-> Typed
./autofuzz.sh run $image python3.9 47 2 typed
fi

if [ "$rq" == "rq2.2" ] || [ "$rq" == "rq2" ] || [ "$rq" == "all" ]; then
# 2.2 for complexity: 1 -> 4 → 16 → 64 → 256 → 1024 → 4096
./autofuzz.sh run $image python3.9 1 1 compl 1
./autofuzz.sh run $image python3.9 2 1 compl 4
./autofuzz.sh run $image python3.9 3 1 compl 16
./autofuzz.sh run $image python3.9 4 1 compl 64
./autofuzz.sh run $image python3.9 5 1 compl 256
./autofuzz.sh run $image python3.9 6 1 compl 1024
./autofuzz.sh run $image python3.9 7 1 compl 4096
fi

# 2.3 built-in CMD: Normal vs. Abnormal
if [ "$rq" == "rq2.3" ] || [ "$rq" == "rq2" ] || [ "$rq" == "all" ]; then
./autofuzz.sh run $image python3.9 8 2 bncmd
fi
