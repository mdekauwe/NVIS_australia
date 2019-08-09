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
import glob
import xarray as xr
import netCDF4 as nc
import datetime
import os
import sys
import shutil
import netCDF4

def main():

    in_fname = "/Users/mdekauwe/Desktop/gridinfo_mmy_MD_elev_orig_std_avg-sand_mask.nc"
    out_fname = "/Users/mdekauwe/Desktop/gridinfo_mmy_MD_elev_orig_std_avg-sand_mask_new_pfts.nc"
    iveg_fname = "data/SE_aus_veg_types_0.5deg.nc"

    ds = xr.open_dataset(in_fname)
    ds_iveg = xr.open_dataset(iveg_fname)

    lc = ds_iveg.iveg.values
    lc = lc.astype(np.int16)
    lc = np.where(lc <= 18, -1, lc) # Mask the rest
    lc = np.where(ds.iveg > 0, lc, -1)
    
    ds_out = ds.copy(deep=True)
    ds_out = ds_out.drop("iveg")

    ds_out.to_netcdf(out_fname)
    ds_out.close()

    f = netCDF4.Dataset(out_fname, 'r+')

    nc_attrs = f.ncattrs()
    nc_dims = [dim for dim in f.dimensions]
    nc_vars = [var for var in f.variables]

    iveg = f.createVariable("iveg", 'i4', ('latitude', 'longitude'))
    iveg.long_name = "CSIRO classification of veg type"
    iveg.missing_value = -1

    iveg[:,:] = lc
    f.close()

    ds.close()
    ds_iveg.close()

if __name__ == "__main__":

    main()
