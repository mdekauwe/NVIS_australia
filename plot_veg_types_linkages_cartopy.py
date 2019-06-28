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
import cartopy.crs as ccrs
import cartopy
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import sys

fname = "data/SE_aus_veg_types.nc"

ds = xr.open_dataset(fname)

lc = ds.biome_code.values
lat = ds.latitude.values
lon = ds.longitude.values



top, bottom = lat[0], lat[-1]
left, right = lon[0], lon[-1]

fig = plt.figure(figsize=(9,6))
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.sans-serif'] = "Helvetica"

ax = plt.axes(projection=ccrs.PlateCarree())

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.5,
                  color='black', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_right = False
gl.xlines = False
gl.ylines = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
ax.coastlines(resolution='10m', linewidth=1.0, color='black')



cmap = plt.cm.viridis
bounds = np.arange(1,10)
norm = colors.BoundaryNorm(bounds, cmap.N)
labels = ["RAF", "WSF", "DSF", "GRW", "SAW", "MIF", "SHB", "GRA"]


img = ax.imshow(lc, origin='upper', transform=ccrs.PlateCarree(),
                interpolation='nearest', cmap=cmap, norm=norm,
                extent=(left, right, bottom, top))
cbar = plt.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds, ticks=bounds)
cbar.set_ticklabels(labels)
tick_locs = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
cbar.set_ticks(tick_locs)

#ax.set_ylabel("Latitude")
#ax.set_xlabel("Longtiude")
ax.text(-0.10, 0.55, 'Latitude', va='bottom', ha='center',
        rotation='vertical', rotation_mode='anchor',
        transform=ax.transAxes)
ax.text(0.5, -0.1, 'Longitude', va='bottom', ha='center',
        rotation='horizontal', rotation_mode='anchor',
        transform=ax.transAxes)
#

fig.savefig("SE_AUS_veg_types.png", dpi=150)
sys.exit()

cmap = plt.cm.viridis
bounds = np.arange(1,10) # 2 more than the number of classes = 8
#print(bounds)
#print(len(bounds))
norm = colors.BoundaryNorm(bounds, cmap.N)
labels = ["RAF", "WSF", "DSF", "GRW", "SAW", "MIF", "SHB", "GRA"]


img = ax.imshow(lc, origin='upper', interpolation='nearest',
                 cmap=cmap, norm=norm)
cbar = plt.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds, ticks=bounds)
cbar.set_ticklabels(labels)
tick_locs = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
cbar.set_ticks(tick_locs)

#plt.show()
fig.savefig("SE_AUS_veg_types.png", dpi=150)
