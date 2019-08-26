library(raster)

veg <- raster("data/SE_aus_veg_types.nc")

#NB first had to run ./fix_lat_lon.sh
gswp <- raster("/Users/mdekauwe/Desktop/awap_grid_file_for_martin.nc")
regrid <- resample(veg, gswp, method="ngb") # nearest neighbour
writeRaster(regrid, "data/SE_aus_veg_types_AWAP_grid.nc", varname="iveg", overwrite=TRUE)
