# maps_analysis
Download your Google data here
https://takeout.google.com/?hl=da&utm_source=google-account&utm_medium=web

(1) Use json2csv.py to convert the JSON file to a CSV file that is easier to work with.

The csv has format

`
,accuracy,lat,long,time
`

(2) Use clustering.py to cluster the lat long coordinates with no timestamps included.
It is saved as latlongClusters.png
