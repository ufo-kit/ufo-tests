#!/bin/bash

out=$1

ufo-launch dummy-data width=1 height=1 ! opencl filename=test-opencl-pass-options.cl kernel=f options="'-DFOO=1234'" ! write filename=$out
