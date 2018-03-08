#!/bin/bash
# epsilon: 0.0001

ufo-launch --quiet \
    read path=data/lena.tif ! \
    fft dimensions=2 ! ifft dimensions=2 ! \
    write filename=$1
