#!/bin/bash

#cdo remapnn,/Users/mdekauwe/Desktop/GSWP3.BC.Tair.3hrMap.1929.nc  \
#            data/SE_aus_veg_types.nc \
#            data/E_aus_veg_types_AWAP_grid.nc

#cdo remapcon,/Users/mdekauwe/Desktop/GSWP3.BC.Tair.3hrMap.1929.nc  \
#            data/SE_aus_veg_types.nc \
#            data/E_aus_veg_types_AWAP_grid.nc


cdo remapnn,/Users/mdekauwe/Desktop/awap_grid_file_for_martin.nc  \
            data/SE_aus_veg_types.nc \
            data/SE_aus_veg_types_AWAP_grid.nc
