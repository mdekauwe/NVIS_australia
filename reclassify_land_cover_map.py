#!/usr/bin/env python
"""
Reclassify the NVIS classes to make a 6 class land-cover map of SE Australia.

The vegetation classes we are aiming to create here are: Rainforest,
Eucalypt Forests, Acacia Forests and Woodlands,
Miscellaneous Forests and Woodlands, Shurblands, Grasslands, Other (mask)

That's all folks.
"""
__author__ = "Martin De Kauwe"
__version__ = "1.0 (27.06.2019)"
__email__ = "mdekauwe@gmail.com"


import xarray as xr
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


fname = "data/SE_aus_reprojected_NVIS.nc"
out_fname = "data/SE_aus_veg_types.nc"
ds = xr.open_dataset(fname)
lc = ds.biome_code

# Fact sheet explanation to classes:
# https://www.environment.gov.au/land/publications/nvis-fact-sheet-series-4-2

# rainforest
lc = np.where(lc == 1, 0, lc)  # Rainforests and vine thickets

# Eucalypt Forests
lc = np.where(lc == 2, 1, lc) # Eucalypt tall open forests, are equivalent to the concept of ‘wet sclerophyll forest’,
lc = np.where(lc == 3, 1, lc) # Eucalypt open forests: correspond well with ‘dry sclerophyll forests’,
lc = np.where(lc == 4, 1, lc) # Eucalypt low open forests
lc = np.where(lc == 5, 1, lc) # Eucalypt woodlands
lc = np.where(lc == 11, 1, lc) # Eucalypt open woodlands
lc = np.where(lc == 12, 1, lc) # Tropical eucalypt woodlands/grasslands

# Acacia Forests and Woodlands
lc = np.where(lc == 6, 2, lc) # Acacia forests and woodlands
lc = np.where(lc == 13, 2, lc) # Acacia open woodlands

# Miscellaneous Forests and Woodlands
lc = np.where(lc == 7, 3, lc) # Callitris forests and woodlands
lc = np.where(lc == 8, 3, lc) # Casuarina forests and woodlands
lc = np.where(lc == 9, 3, lc) # Melaleuca forests and woodlands
lc = np.where(lc == 23, 3, lc) # Mangroves
lc = np.where(lc == 10, 3, lc) # Other forests and woodlands

# Shurblands
lc = np.where(lc == 14, 4, lc) # Mallee woodlands and shrublands
lc = np.where(lc == 15, 4, lc) # Low closed forests and tall closed shrublands
lc = np.where(lc == 16, 4, lc) # Acacia shrublands
lc = np.where(lc == 17, 4, lc) # Other shrublands
lc = np.where(lc == 22, 4, lc) # Chenopod shrublands, samphire shrublands and forblands
lc = np.where(lc == 18, 4, lc) # Heathlands

# Grasslands
lc = np.where(lc == 19, 5, lc) # Tussock grasslands
lc = np.where(lc == 20, 5, lc) # Hummock grasslands
lc = np.where(lc == 21, 5, lc) # Other grasslands, herblands, sedgelands and rushlands

# Other - mask
lc = np.where(lc >= 24, 6, lc) # Mask


ax1 = plt.imshow(lc, origin='upper')
plt.colorbar()
#cmap = plt.cm.jet  # define the colormap

# extract all colors from the .jet map
#cmaplist = [cmap(i) for i in range(cmap.N)]

# force the first color entry to be white
#cmaplist[0] = (0, 0, 0, 1.0)

# create the new map
#cmap = mpl.colors.LinearSegmentedColormap.from_list('Custom cmap', cmaplist, cmap.N)

#bounds = np.linspace(0, 6, 6)
#norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
#cb = plt.colorbar.ColorbarBase(ax1, cmap=cmap, norm=norm,
#                               spacing='proportional', ticks=bounds,
#                               boundaries=bounds, format='%1i')

plt.show()

#lc.to_netcdf(out_fname)
