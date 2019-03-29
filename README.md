# maps_analysis
Download your Google data here
https://takeout.google.com/?hl=da&utm_source=google-account&utm_medium=web

You only need to download your Google Maps data, but I think everyone should download
all their data to feel empowered (mine are around I believe 10GB compressed).

(1) Use json2csv.py to convert the JSON file to a CSV file that is easier to work with.

The csv has format

`
,accuracy,lat,long,time
0,20,562218374,97452201,1514641794572
1,91,562218678,97449370,1514641810000
2,64,562218678,97449370,1514641948205
`

(2) Use clustering.py to cluster the lat long coordinates with no timestamps included.
It is saved as latlongClusters.png