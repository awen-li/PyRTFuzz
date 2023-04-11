#!/bin/bash

mkdir temp
find ./ -name "crash-*" | xargs -i cp {} ./temp
find ./ -name "slow-unit-*" | xargs -i cp {} ./temp

cd temp
python -m pycollect
cat History.hty | wc -l
