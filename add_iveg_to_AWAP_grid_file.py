#!/usr/bin/env python

"""
Add the newly created iveg PFTs to the CABLE gridinfo file

That's all folks.
"""
__author__ = "Martin De Kauwe"
__version__ = "1.0 (01.08.2019)"
__email__ = "mdekauwe@gmail.com"

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import os
import sys
from os.path import join

def main(grid_path, grid_fname, nvis_iveg_fname, out_grid_fname):

    source = xr.open_dataset(join(grid_path, grid_fname))

    # File with new linkages veg types.
    se_aus = xr.open_dataset(nvis_iveg_fname)

    # AWAP data is upside down, flip it
    se_aus["iveg"][:,:] = np.flipud(se_aus["iveg"][:,:])

    # Rounding issue on the lat lon, so they won't match, just use the
    # AWAP grid vals.
    se_aus["latitude"] = source["latitude"]
    se_aus["longitude"] = source["longitude"]



    #plt.plot(se_aus["latitude"])
    #plt.plot(source["latitude"])
    #plt.show()
    #sys.exit()
    # First had to do
    # cdo sellonlatbox,112,154,-44,-10 data/SE_aus_veg_types_AWAP_grid.nc data/SE_aus_veg_types_AWAP_fixed_grid.nc
    #out_grid_fname = "/Users/mdekauwe/Desktop/SE_aus_veg_types_AWAP_grid.nc"

    # This is the original values
    #source.iveg.plot(vmin=0, vmax=22)

    # Netcdf metadata with the type and fill value
    source.iveg.encoding
    #print (source.iveg.encoding)
    #print(source.iveg.encoding['_FillValue'])
    # The new values to use
    #se_aus.iveg.plot(vmin=0, vmax=22)

    # Merge the two fields
    # Where se_aus.iveg is defined (found using numpy.isfinite) use the values
    # from se_aus.iveg
    # Elsewhere use the original values from source.iveg
    merged_iveg = xr.where(np.isfinite(se_aus.iveg), se_aus.iveg, source.iveg.encoding['_FillValue'])
    #merged_iveg.plot(vmin=0, vmax=22)

    # Copy the netcdf metadata to the new field (type, missing values)
    merged_iveg.encoding = source.iveg.encoding

    # Maintain the same land-sea pixels.
    #merged_iveg = xr.where(np.isnan(source.iveg), -1, merged_iveg)
    #merged_iveg = xr.where(np.isnan(source.iveg), source.iveg.encoding['_FillValue'], merged_iveg)
    #merged_iveg = xr.where(np.logical_or(source.iveg < -500.0, np.isnan(source.iveg)), -9999.0, merged_iveg)

    # Replace the source dataset's iveg field with the new version and save to
    # file
    source['iveg'] = merged_iveg

    source.to_netcdf(os.path.join(grid_path, out_grid_fname))

if __name__ == "__main__":

    # CSIRO soil
    grid_path = "/Users/mdekauwe/Desktop/SE_AUS_AWAP_grid_mask_files/raw/grid"
    grid_fname = "gridinfo_AWAP_CSIRO_AU_NAT.nc"
    nvis_iveg_fname = "data/SE_aus_veg_types_AWAP_grid.nc"
    out_grid_fname = "/Users/mdekauwe/Desktop/SE_AU_AWAP_NVIS_iveg_csiro_soil_grid.nc"
    main(grid_path, grid_fname, nvis_iveg_fname, out_grid_fname)

    # OpenLand soil
    grid_path = "/Users/mdekauwe/Desktop/SE_AUS_AWAP_grid_mask_files/raw/grid"
    grid_fname = "gridinfo_AWAP_OpenLandMap.nc"
    nvis_iveg_fname = "data/SE_aus_veg_types_AWAP_grid.nc"
    out_grid_fname = "/Users/mdekauwe/Desktop/SE_AU_AWAP_NVIS_iveg_openland_soil_grid.nc"
    main(grid_path, grid_fname, nvis_iveg_fname, out_grid_fname)
