#!/usr/bin/env python

"""
Generate six vegetation types land cover map for NSW

That's all folks.
"""
__author__ = "Martin De Kauwe"
__version__ = "1.0 (19.06.2019)"
__email__ = "mdekauwe@gmail.com"

import os
import sys
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr

def main(fname):

    ds = xr.open_dataset(fname)

    print(ds)


if __name__ == "__main__":

    fname = "data/nvis_data_raster.nc"
    main(fname)
