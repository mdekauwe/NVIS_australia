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
out_fname = "data/SE_aus_veg_types.nc"
ds = xr.open_dataset(fname)
lc = ds.biome_code
lc = lc.astype(np.int16)


"""
cmap = plt.cm.viridis
bounds = np.arange(23)
norm = colors.BoundaryNorm(bounds, cmap.N)
img = plt.imshow(lc, origin='upper', interpolation='nearest',
                 cmap=cmap, norm=norm)
plt.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds, ticks=bounds)
plt.show()
sys.exit()
"""

# Fact sheet explanation to classes:
# https://www.environment.gov.au/land/publications/nvis-fact-sheet-series-4-2


# Miscellaneous Forests and Woodlands
lc = np.where(lc == 8, 1, lc) # Casuarina forests and woodlands
lc = np.where(lc == 10, 2, lc) # Other forests and woodlands
lc = np.where(lc == 31, 3, lc) # Other open woodlands
lc = np.where(lc == 29, 4, lc) # Regrowth, modified native vegetation



# Other - mask
lc = np.where(lc == 24, np.nan, lc) # Inland aquatic: freshwater, salt lakes, lagoons
lc = np.where(lc == 27, np.nan, lc) # Naturally bare: sand, rock, claypan, mudflat
lc = np.where(lc == 28, np.nan, lc) # Sea and estuaries
lc = np.where(lc == 99, np.nan, lc) # Unknown/no data
lc = np.where(lc == 9, np.nan, lc) # Melaleuca forests and woodlands
lc = np.where(lc == 23, np.nan, lc) # Mangroves
lc = np.where(lc == 21, np.nan, lc) # Other grasslands, herblands, sedgelands and rushlands
lc = np.where(lc == 30, np.nan, lc) # Unclassified forest
#vals = np.unique(lc[~np.isnan(lc)])
#for v in vals:
#    print(v)
lc = np.where(lc >= 5, np.nan, lc) # Mask the rest
lc = np.where(lc < 1, np.nan, lc)  # Mask the rest

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

#ds['biome_code'][:,:] = lc
#ds.to_netcdf(out_fname)
