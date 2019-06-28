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
import numpy as np
from matplotlib import colors

fname = "data/SE_aus_veg_types.nc"

ds = xr.open_dataset(fname)
lc = ds.biome_code.values


fig = plt.figure(figsize=(9,6))
cmap = plt.cm.viridis

bounds = np.unique(lc[~np.isnan(lc)])
bounds = np.append(bounds, bounds[-1]+1)

print(bounds)

norm = colors.BoundaryNorm(bounds, cmap.N)
img = plt.imshow(lc, origin='upper', interpolation='nearest',
                 cmap=cmap, norm=norm)
cbar = plt.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds, ticks=bounds)
tick_locs = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5]
cbar.set_ticks(tick_locs)

plt.show()
#fig.savefig("SE_AUS_veg_types_misc.png", dpi=150)
