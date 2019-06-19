#!/usr/bin/env python

"""
Generate six vegetation types land cover map for NSW

That's all folks.
"""
__author__ = "Martin De Kauwe"
__version__ = "1.0 (19.06.2019)"
__email__ = "mdekauwe@gmail.com"

import os
import sys
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr


def main(fname):

    ds = xr.open_dataset(fname)


    # subset by NSW-ish, extending through victoria too.
    # cdo sellonlatbox,138., 154.,-40.0, -28. in.nc out.nc
    lat_bounds = [-40.0, -28.]
    lon_bounds = [138., 154.]
    bounds = lat_bounds + lon_bounds

    """
    lats = ds['latitude'][:]
    lons = ds['longitude'][:]
    latli = np.argmin(np.abs(lats - lat_bounds[1])).values
    latui = np.argmin(np.abs(lats - lat_bounds[0])).values
    lonli = np.argmin(np.abs(lons - lon_bounds[0])).values
    lonui = np.argmin(np.abs(lons - lon_bounds[1])).values
    """

    #print([latli.values,latui,lonli,lonui])
    #[latli:latui,lonli:lonui]

    #print(np.unique(biomes))
    #print(ds.biome_code[latli:latui,lonli:lonui].shape)
    #plt.imshow(ds.biome_code)
    #plt.colorbar()
    #plt.show()

if __name__ == "__main__":

    fname = "data/nvis_data_raster.nc"
    main(fname)
