# NVIS Australia

Repository to generate PFT map for drought simulations. This relies on the original NetCDF file that Anna made from the raw data, found:

/srv/ccrc/data04/z3509830/LAI_precip_variability/GRID_NVIS4_2_AUST_EXT_MVG

```bash
$ ./subset_NVIS_for_SE_aus.py
$ ./reclassify_land_cover_map_linkages.py
$ ./fix_lat_lon.sh
$ Rscript ./regrid_NVIS_data_to_0.5deg.R
$ ./add_iveg_to_grid_file.py
```

## Contacts

* [Martin De Kauwe](http://mdekauwe.github.io/)
