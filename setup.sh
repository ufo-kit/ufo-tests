#!/bin/sh

wget -q -A tif -nH -r --cut-dirs=2 http://www.ipe.fzk.de/~vogelgesang/ufo-tests
rm -f robots.txt.tmp
