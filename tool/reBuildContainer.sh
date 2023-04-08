docker stop $(docker ps -a -f "name=cpyfuzz")
docker rm $(docker ps -a -f "name=cpyfuzz")
./autofuzz.sh run daybreak2019/prtfuzz:v1.1 python3.9 0 10
./autofuzz.sh run daybreak2019/prtfuzz:v1.1 python3.8 44 10
./autofuzz.sh run daybreak2019/prtfuzz:v1.1 python3.7 54 10
