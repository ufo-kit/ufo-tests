#!/bin/bash
# epsilon: 0.0001

ufo-launch --quiet \
    read path=data/lena.tif ! \
    fft ! ifft ! \
    write filename=$1
