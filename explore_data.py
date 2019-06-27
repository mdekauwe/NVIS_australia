#!/usr/bin/env python
"""
Explore the SE Aus subset with a view to making a 6 class landcover map

That's all folks.
"""
__author__ = "Martin De Kauwe"
__version__ = "1.0 (27.06.2019)"
__email__ = "mdekauwe@gmail.com"


import xarray as xr
import matplotlib.pyplot as plt

fname = "data/SE_aus_reprojected_NVIS.nc"

ds = xr.open_dataset(fname)

plt.imshow(ds.biome_code, origin='upper')
plt.colorbar()
plt.show()
