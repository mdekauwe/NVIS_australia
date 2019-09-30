library(raster)


veg <- raster("data/SE_aus_veg_types.nc")

gswp <- raster("/Users/mdekauwe/Desktop/AWAP.Tair.3hr.2000.nc")
regrid <- resample(veg, gswp, method="ngb") # nearest neighbour
writeRaster(regrid, "data/SE_aus_veg_types_AWAP_grid.nc", varname="iveg", overwrite=TRUE)
