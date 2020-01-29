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

def main():

    path = "/Users/mdekauwe/Desktop/SE_AUS_AWAP_grid_mask_files/raw"
    #path = "/g/data1a/w35/mgk576/research/CABLE_runs/cms"
    #source = xr.open_dataset(join(path,
    #                         'MD_elev_orig_std_avg-sand_AWAP_AU_mask.nc'))
    source = xr.open_dataset(join(path,
                             'gridinfo_AWAP_CSIRO_AU_NAT.nc'))

    se_aus = xr.open_dataset('data/SE_aus_veg_types_AWAP_grid.nc')

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
    out_grid_fname = "/Users/mdekauwe/Desktop/SE_aus_veg_types_AWAP_grid.nc"

    # This is the original values
    #source.iveg.plot(vmin=0, vmax=22)

    # Netcdf metadata with the type and fill value
    source.iveg.encoding
    print (source.iveg.encoding)
    print(source.iveg.encoding['_FillValue'])
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

    source.to_netcdf(os.path.join(path, out_grid_fname))

if __name__ == "__main__":

    main()
