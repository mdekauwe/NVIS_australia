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

def main():

    fdir = "/Users/mdekauwe/Desktop/"
    grid_fname = "gridinfo_mmy_MD_elev_orig_std_avg-sand_mask.nc"
    out_grid_fname = "gridinfo_mmy_MD_elev_orig_std_avg-sand_mask_new_pfts.nc"
    in_fname = os.path.join(fdir, grid_fname)
    out_fname = os.path.join(fdir, out_grid_fname)
    iveg_fname = "data/SE_aus_veg_types_0.5deg.nc"

    ds = xr.open_dataset(in_fname)
    ds_iveg = xr.open_dataset(iveg_fname)

    ds_iveg['iveg'] = ds_iveg.iveg.fillna(-1).astype('i4')

    # NVIS regridding has some pixels in the sea, match the original grid
    ds_iveg['iveg'] = xr.where(np.isnan(ds.iveg), -1, ds_iveg['iveg'])
    ds_iveg['iveg'].attrs={'long_name':'iveg', 'min':19,
                           'max':22, 'missing_value':-1}



    ds_out = ds.copy(deep=True)
    ds_out = ds_out.drop("iveg")
    ds_out['iveg'] = ds_iveg['iveg']
    ds_out.to_netcdf(out_fname)

    ds.close()
    ds_out.close()
    ds_iveg.close()

if __name__ == "__main__":

    main()
