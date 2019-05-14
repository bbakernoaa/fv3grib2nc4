# fv3grib2nc4


This is a simple utility to help with aerosol grib data from NCEP for python

To use you can pass single or multiple files

```
fv3grib2nc4.py -v -f "gfs.t00z.master.grb2f00*"
```

This will output three files for each grib file base on the level for aerosols from NCEP POST.

- 1 hybrid level
- entire atmosphere
- surface

