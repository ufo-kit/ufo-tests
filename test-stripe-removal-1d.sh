#!/bin/bash
# epsilon: 0.1

ufo-launch --quiet \
    read path=data/test-stripe-removal-input.tif ! \
    transpose ! \
    fft dimensions=1 ! filter-stripes1d strength=2 ! ifft dimensions=1 crop-width=3000 ! \
    transpose ! \
    write filename=$1
