Readme.txt
==========

Creation Date: 01/02/2016
Revision Date: 01/02/2016


ZIP PACKAGE
------------

This zip package contains:

- An ArcGIS GRID Raster for Major Vegetation Groups - Australia wide - EXTANT (The Value Attribute Table includes the following attributes: VALUE (MVG Number), MVG_NAME, MVG_COMMON_DESC and SORT_ORDER). See metadata for details.
- Relevant layer files for this raster


NVIS 4.2 MVG RASTER SYMBOLOGY
-----------------------------

This GRID Raster has an applied colormap based on the standard NVIS MVG legend colour scheme. However, this colormap provides only MVG Number values when displaying the Symbology in ArcGIS. 

To enable full MVG Descriptions to appear in the legend (sorted by NAME or NUMBER), the included layer files will need to be imported via ArcGIS Symbology and the relevant field (see below) chosen from the list of attributes.

- mvg4_2e_by_name.lyr (use MVG NAME)
- mvg4_2e_by_number.lyr (use VALUE)