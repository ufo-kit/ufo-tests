#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: runner.sh test-script.sh"
    exit 1
fi

prog=$1
name=${prog%.sh}
output="output/$name-output.tif"
ref="reference/$name-ref.tif"
epsilon=$(grep -E "#[ ]*epsilon:[ ]*[0-9][0-9]*\.[0-9]+" $prog | grep -oE "[0-9][0-9]*\.[0-9]+")

if [ -z "$epsilon" ]; then
    epsilon="0.0"
fi

time=$(bash $prog $output)
rmse=$(python helper/compare.py --input $output --reference $ref --epsilon $epsilon)

if [[ $? != 0 ]]; then
    echo "$(tput setaf 1)FAIL$(tput sgr0)  $name (RMSE = $rmse)"
else
    echo "$(tput setaf 2)PASS$(tput sgr0)  $name (RMSE = $rmse)"
fi
