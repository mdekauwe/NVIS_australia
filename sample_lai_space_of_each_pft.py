#!/usr/bin/env python

"""
Get LAI range from each PFT

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

    lai = xr.open_dataset(join("/Users/mdekauwe/Desktop/", 'lai_max.nc'))
    iveg = xr.open_dataset('data/SE_aus_veg_types_5km.nc')
    out_grid_fname = "gridinfo_mmy_MD_elev_orig_std_avg-sand_mask_new_pfts.nc"

    lat_bnds, lon_bnds = [-28, -40], [140, 154]
    #x = iveg.sel(latitude=slice(*lat_bnds), longitude=slice(*lon_bnds))
    #y = lai.sel(latitude=slice(*lat_bnds), longitude=slice(*lon_bnds))
    print(lai)
    print(iveg)

    #lai = lai.sel(latitude=slice(*lat_bnds), longitude=slice(*lon_bnds))

    #plt.imshow(iveg.iveg[:,:])
    #plt.show()




if __name__ == "__main__":

    main()
