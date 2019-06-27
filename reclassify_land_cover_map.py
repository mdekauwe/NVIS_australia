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

# rainforest
lc = np.where(lc == 1, 1, lc)  # Rainforests and vine thickets

# Eucalypt Forests
lc = np.where(lc == 2, 2, lc) # Eucalypt tall open forests, are equivalent to the concept of ‘wet sclerophyll forest’,
lc = np.where(lc == 3, 2, lc) # Eucalypt open forests: correspond well with ‘dry sclerophyll forests’,
lc = np.where(lc == 4, 2, lc) # Eucalypt low open forests
lc = np.where(lc == 5, 2, lc) # Eucalypt woodlands
lc = np.where(lc == 11, 2, lc) # Eucalypt open woodlands
lc = np.where(lc == 12, 2, lc) # Tropical eucalypt woodlands/grasslands

# Acacia Forests and Woodlands
lc = np.where(lc == 6, 3, lc) # Acacia forests and woodlands
lc = np.where(lc == 13, 3, lc) # Acacia open woodlands

# Miscellaneous Forests and Woodlands
lc = np.where(lc == 7, 4, lc) # Callitris forests and woodlands
lc = np.where(lc == 8, 4, lc) # Casuarina forests and woodlands
lc = np.where(lc == 9, 4, lc) # Melaleuca forests and woodlands
lc = np.where(lc == 23, 4, lc) # Mangroves
lc = np.where(lc == 10, 4, lc) # Other forests and woodlands

# Shurblands
lc = np.where(lc == 14, 5, lc) # Mallee woodlands and shrublands
lc = np.where(lc == 15, 5, lc) # Low closed forests and tall closed shrublands
lc = np.where(lc == 16, 5, lc) # Acacia shrublands
lc = np.where(lc == 17, 5, lc) # Other shrublands
lc = np.where(lc == 22, 5, lc) # Chenopod shrublands, samphire shrublands and forblands
lc = np.where(lc == 18, 5, lc) # Heathlands

# Grasslands
lc = np.where(lc == 19, 6, lc) # Tussock grasslands
lc = np.where(lc == 20, 6, lc) # Hummock grasslands
lc = np.where(lc == 21, 6, lc) # Other grasslands, herblands, sedgelands and rushlands

# Other - mask
lc = np.where(lc >= 24, np.nan, lc) # Mask

print(np.nanmin(lc), np.nanmax(lc))

fig = plt.figure()
cmap = plt.cm.viridis
bounds = np.arange(8)
norm = colors.BoundaryNorm(bounds, cmap.N)
img = plt.imshow(lc, origin='upper', interpolation='nearest',
                 cmap=cmap, norm=norm)
plt.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds, ticks=bounds)
#plt.show()
fig.savefig("SE_AUS_veg_types.png", dpi=150)

ds['biome_code'] = lc

ds.to_netcdf(out_fname)
