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
import netCDF4

fname = "data/SE_aus_reprojected_NVIS.nc"
out_fname = "data/SE_aus_veg_types.nc"
ds = xr.open_dataset(fname)

ds_out = ds.copy(deep=True)
ds_out = ds_out.drop("biome_code")

ds_out.to_netcdf(out_fname)
ds_out.close()


f = netCDF4.Dataset(out_fname, 'r+')

nc_attrs = f.ncattrs()
nc_dims = [dim for dim in f.dimensions]
nc_vars = [var for var in f.variables]

iveg = f.createVariable("iveg", 'i4', ('latitude', 'longitude'))
iveg.long_name = "CSIRO classification of veg type"
iveg.missing_value = -1


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

# Rainforest
lc = np.where(lc == 1, 1, lc)  # Rainforests and vine thickets

# Wet sclerophyll forest
lc = np.where(lc == 2, 2, lc) # Eucalypt tall open forests, are equivalent to the concept of ‘wet sclerophyll forest’,
lc = np.where(lc == 10, 2, lc) # Other forests and woodlands
lc = np.where(lc == 8, 2, lc) # Casuarina forests and woodlands

# Dry sclerophyll forest
lc = np.where(lc == 3, 3, lc) # Eucalypt open forests: correspond well with ‘dry sclerophyll forests’,
lc = np.where(lc == 4, 3, lc) # Eucalypt low open forests
lc = np.where(lc == 7, 3, lc) # Callitris forests and woodlands
lc = np.where(lc == 31, 3, lc) # Other open woodlands

# Grassy woodlands
lc = np.where(lc == 5, 4, lc) # Eucalypt woodlands
lc = np.where(lc == 11, 4, lc) # Eucalypt open woodlands
lc = np.where(lc == 12, 4, lc) # Tropical eucalypt woodlands/grasslands
lc = np.where(lc == 25, 4, lc) # Cleared, non-native vegetation, buildings
lc = np.where(lc == 29, 4, lc) # Regrowth, modified native vegetation

# Semiarid woodland
lc = np.where(lc == 6, 5, lc) # Acacia forests and woodlands
lc = np.where(lc == 13, 5, lc) # Acacia open woodlands
lc = np.where(lc == 14, 5, lc) # Mallee woodlands and shrublands
lc = np.where(lc == 16, 5, lc) # Acacia shrublands
lc = np.where(lc == 32, 5, lc) # Mallee open woodlands and sparse mallee shrublands
lc = np.where(lc == 15, 5, lc) # Low closed forests and tall closed shrublands
lc = np.where(lc == 17, 5, lc) # Other shrublands
lc = np.where(lc == 22, 5, lc) # Chenopod shrublands, samphire shrublands and forblands
lc = np.where(lc == 18, 5, lc) # Heathlands
lc = np.where(lc == 26, 5, lc) # Unclassified native vegetation
lc = np.where(lc == 19, 5, lc) # Tussock grasslands
lc = np.where(lc == 20, 5, lc) # Hummock grasslands

# Miscellaneous Forests and Woodlands
#lc = np.where(lc == 8, 6, lc) # Casuarina forests and woodlands
#lc = np.#
#



# Other - mask
lc = np.where(lc == 24, -1, lc) # Inland aquatic: freshwater, salt lakes, lagoons
lc = np.where(lc == 27, -1, lc) # Naturally bare: sand, rock, claypan, mudflat
lc = np.where(lc == 28, -1, lc) # Sea and estuaries
lc = np.where(lc == 99, -1, lc) # Unknown/no data
lc = np.where(lc == 9, -1, lc) # Melaleuca forests and woodlands
lc = np.where(lc == 23, -1, lc) # Mangroves
lc = np.where(lc == 21, -1, lc) # Other grasslands, herblands, sedgelands and rushlands
lc = np.where(lc == 30, -1, lc) # Unclassified forest
#vals = np.unique(lc[~np.isnan(lc)])
#for v in vals:
#    print(v)
lc = np.where(lc >= 6, -1, lc) # Mask the rest
lc = np.where(lc < 1, -1, lc)  # Mask the rest

lc = np.where(lc == 1, 18, lc)
lc = np.where(lc == 2, 19, lc)
lc = np.where(lc == 3, 20, lc)
lc = np.where(lc == 4, 21, lc)
lc = np.where(lc == 5, 22, lc)
lc = np.where(lc <= 6, -1, lc) # Mask the rest

iveg[:,:] = lc
f.close()

#ds['biome_code'][:,:] = lc
#ds.to_netcdf(out_fname)
#print(out_fname)

ds.close()
