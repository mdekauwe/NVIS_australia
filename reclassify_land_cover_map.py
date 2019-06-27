#!/usr/bin/env python
"""
Reclassify the NVIS classes to make a 6 class land-cover map of SE Australia.

The vegetation classes we are aiming to create here are: rainforest,
wet sclerophyll forest, dry sclerophyll forest, grassy woodland,
semi-arid woodland & other

That's all folks.
"""
__author__ = "Martin De Kauwe"
__version__ = "1.0 (27.06.2019)"
__email__ = "mdekauwe@gmail.com"


import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

fname = "data/SE_aus_reprojected_NVIS.nc"
out_fname = "data/SE_aus_veg_types.nc"
ds = xr.open_dataset(fname)
lc = ds.biome_code

# Fact sheet explanation to classes:
# https://www.environment.gov.au/land/publications/nvis-fact-sheet-series-4-2

# rainforest
lc = np.where(lc == 1, 0, lc)  # Rainforests and vine thickets
lc = np.where(lc == 12, 0, lc) # Tropical eucalypt woodlands/grasslands

# wet sclerophyll forest
lc = np.where(lc == 2, 1, lc) # Eucalypt tall open forests, are equivalent to the concept of ‘wet sclerophyll forest’,

# dry sclerophyll forest
lc = np.where(lc == 3, 2, lc) # Eucalypt open forests: correspond well with ‘dry sclerophyll forests’,

# grassy woodland
lc = np.where(lc == 4, 3, lc) # Eucalypt low open forests
lc = np.where(lc == 5, 3, lc) # Eucalypt woodlands
lc = np.where(lc == 7, 3, lc) # Callitris forests and woodlands
lc = np.where(lc == 8, 3, lc) # Casuarina forests and woodlands
lc = np.where(lc == 9, 3, lc) # Melaleuca forests and woodlands
lc = np.where(lc == 10, 3, lc) # Other forests and woodlands
lc = np.where(lc == 11, 3, lc) # Eucalypt open woodlands

# semi-arid woodland
lc = np.where(lc == 6, 4, lc) # Acacia forests and woodlands
lc = np.where(lc == 13, 4, lc) # Acacia open woodlands
lc = np.where(lc == 14, 4, lc) # Mallee woodlands and shrublands
lc = np.where(lc == 15, 4, lc) # Low closed forests and tall closed shrublands
lc = np.where(lc == 16, 4, lc) # Acacia shrublands
lc = np.where(lc == 32, 4, lc) # Mallee open woodlands and sparse mallee shrublands

# other: grasses & shrubs
lc = np.where(lc == 17, 5, lc) # Other shrublands
lc = np.where(lc == 18, 5, lc) # Heathlands
lc = np.where(lc == 19, 5, lc) # Tussock grasslands
lc = np.where(lc == 20, 5, lc) # Hummock grasslands
lc = np.where(lc == 21, 5, lc) # Other grasslands, herblands, sedgelands and rushlands
lc = np.where(lc == 22, 5, lc) # Chenopod shrublands, samphire shrublands and forblands
lc = np.where(lc == 23, 5, lc) # Mangroves
lc = np.where(np.logical_and(lc >= 24, lc <= 30), 5, lc) # Other cover types

lc = np.where(lc > 30, np.nan, lc)

plt.imshow(lc, origin='upper')
plt.colorbar()
plt.show()

lc.to_netcdf(out_fname)
