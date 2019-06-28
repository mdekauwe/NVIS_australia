#!/usr/bin/env python
"""
Reclassify the NVIS classes to make a 6 class land-cover map of SE Australia.

The vegetation classes we are aiming to create here are: Rainforest,
Eucalypt Forests, Acacia Forests and Woodlands,
Miscellaneous Forests and Woodlands, Shurblands, Grasslands, Other (mask)

See doc/major-veg-map.pdf

That's all folks.
"""
__author__ = "Martin De Kauwe"
__version__ = "1.0 (27.06.2019)"
__email__ = "mdekauwe@gmail.com"


import xarray as xr
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import sys

fname = "data/SE_aus_reprojected_NVIS.nc"
out_fname = "data/SE_aus_veg_types_misc.nc"
ds = xr.open_dataset(fname)
lc = ds.biome_code
lc = lc.astype(np.int16)



lc = np.where(lc == 8, 1, lc) # Casuarina forests and woodlands
lc = np.where(lc == 10, 2, lc) # Other forests and woodlands
lc = np.where(lc == 31, 3, lc) # Other open woodlands
lc = np.where(lc == 29, 4, lc) # Regrowth, modified native vegetation


#vals = np.unique(lc[~np.isnan(lc)])
#for v in vals:
#    print(v)
lc = np.where(lc >= 5, np.nan, lc) # Mask the rest
lc = np.where(lc < 1, np.nan, lc)  # Mask the rest

ds['biome_code'][:,:] = lc
ds.to_netcdf(out_fname)
