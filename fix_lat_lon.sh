#!/bin/bash

FN="/Users/mdekauwe/Desktop/GSWP3.BC.Tair.3hrMap.1929.nc"
TMP="/Users/mdekauwe/Desktop/tmp.nc"
# Fix the longitude issue in the CABLE output files...
cdo sellonlatbox,-180,180,-90,90 $FN $TMP
mv $TMP $FN
