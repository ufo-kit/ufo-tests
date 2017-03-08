#!/bin/bash
# epsilon: 0.07

ufo-launch --quiet \
    read path=data/test-stripe-removal-input.tif ! \
    fft dimensions=2 ! filter-stripes ! ifft dimensions=2 ! crop height=3000 width=825 ! \
    write filename=$1
