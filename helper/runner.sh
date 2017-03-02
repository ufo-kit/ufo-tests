#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: runner.sh test-script.sh"
    exit 1
fi

prog=$1
name=${prog%.sh}
output="output/$name-output.tif"
ref="reference/$name-ref.tif"

time=$(bash $prog $output)
sad=$(python helper/compare.py --input $output --reference $ref)


if [[ $? != 0 ]]; then
    echo "$(tput setaf 1)FAIL$(tput sgr0)  $name (SAD = $sad)"
else
    echo "$(tput setaf 2)PASS$(tput sgr0)  $name"
fi
