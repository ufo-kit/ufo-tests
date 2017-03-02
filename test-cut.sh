#!/bin/bash

ufo-launch --quiet \
    read path=data/lena.tif ! \
    cut width=199 ! \
    write filename=$1
