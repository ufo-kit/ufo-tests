#!/bin/bash

ufo-launch --quiet \
    read path=data/lena.tif ! \
    crop x=24 y=1 width=384 height=257 ! \
    write filename=$1

