library(raster)

veg <- raster("data/SE_aus_veg_types.nc")

#NB first had to run ./fix_lat_lon.sh
gswp <- raster("/Users/mdekauwe/Desktop/GSWP3.BC.Tair.3hrMap.1929.nc")
regrid <- resample(veg, gswp, method="ngb") # nearest neighbour
writeRaster(regrid, "data/SE_aus_veg_types_0.5deg.nc", varname="iveg", overwrite=TRUE)
