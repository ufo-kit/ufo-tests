#!/bin/bash

rm -f output/*.tif

for script in test-*.sh; do
    ./helper/runner.sh $script
done
