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

    path = "/Users/mdekauwe/Desktop/"
    #path = "/g/data1a/w35/mgk576/research/CABLE_runs/cms"
    source = xr.open_dataset(join(path,
                             'gridinfo_mmy_MD_elev_orig_std_avg-sand_mask.nc'))

    se_aus = xr.open_dataset('data/SE_aus_veg_types_0.5deg.nc')
    out_grid_fname = "gridinfo_mmy_MD_elev_orig_std_avg-sand_mask_new_pfts.nc"

    # This is the original values
    #source.iveg.plot(vmin=0, vmax=22)

    # Netcdf metadata with the type and fill value
    source.iveg.encoding

    # The new values to use
    #se_aus.iveg.plot(vmin=0, vmax=22)

    # Merge the two fields
    # Where se_aus.iveg is defined (found using numpy.isfinite) use the values
    # from se_aus.iveg
    # Elsewhere use the original values from source.iveg
    merged_iveg = xr.where(np.isfinite(se_aus.iveg), se_aus.iveg, source.iveg)
    merged_iveg.plot(vmin=0, vmax=22)

    # Copy the netcdf metadata to the new field (type, missing values)
    merged_iveg.encoding = source.iveg.encoding

    # Maintain the same land-sea pixels.
    merged_iveg = xr.where(np.isnan(source.iveg), -1, merged_iveg)

    # Replace the source dataset's iveg field with the new version and save to
    # file
    source['iveg'] = merged_iveg

    source.to_netcdf(os.path.join(path, out_grid_fname))

if __name__ == "__main__":

    main()
