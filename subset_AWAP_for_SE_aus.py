#!/usr/bin/env python
"""
Subset NVIS file for SE Aus.

Original data from the netcdf Anna made

/srv/ccrc/data04/z3509830/LAI_precip_variability/GRID_NVIS4_2_AUST_EXT_MVG

That's all folks.
"""
__author__ = "Martin De Kauwe"
__version__ = "1.0 (27.06.2019)"
__email__ = "mdekauwe@gmail.com"


import xarray as xr
import matplotlib.pyplot as plt

fname = "data/raw_data/awap_grid.nc"
out_fname = "data/SE_aus_awap_grid.nc"

ds = xr.open_dataset(fname)

lat_bnds, lon_bnds = [-28, -40], [140, 154]
ds = ds.sel(lat=slice(*lat_bnds), lon=slice(*lon_bnds))

#plt.imshow(ds.biome_code, origin='upper')
#plt.colorbar()
#plt.show()

ds.to_netcdf(out_fname)
