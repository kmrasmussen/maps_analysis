# data set is stored as json
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# clustering using KMeans
from sklearn.cluster import KMeans

# gets a list of location objects as they appear in the json file
def getLocationList():
    # open the file
    locationFile = open('dataset.json')
    # get the contents of the file
    fileContent = locationFile.read().replace('\n','')
    # parse the json. There is only one element in the object, namely locations
    locations = json.loads(fileContent)['locations']
    return(locations)

# elements in list may differ, some have special properties.
# They all seem to have timestampMs, longitude, latitude and accuracy
def printSimpleStats():
    timestampCounter = 0
    longitudeCounter = 0
    latitudeCounter = 0
    accuracyCounter = 0
    activityCounter = 0
    for location in locations:
        if 'timestampMs' in location:
            timestampCounter += 1
        if 'latitudeE7' in location:
            latitudeCounter += 1
        if 'longitudeE7' in location:
            longitudeCounter += 1
        if 'accuracy' in location:
            accuracyCounter += 1
        if 'activity' in location:
            activityCounter += 1

    print('total #:' + str(len(locations)))
    print('# has timestamp: ' + str(timestampCounter))
    print('# has latitude: ' + str(latitudeCounter))
    print('# has longtitude: ' + str(longitudeCounter))
    print('# has accuracy: ' + str(accuracyCounter))
    print('# has activity: '+ str(activityCounter))

# turn the list of locations into a pandas dataframe
# for easier working
def makeDataFrame(locations):
    protoDf = []
    for location in locations:
        protoDf.append(
            {
                'time': location['timestampMs'],
                'lat': location['latitudeE7'],
                'long': location['longitudeE7'],
                'accuracy': location['accuracy']
            }
        )
    return(pd.DataFrame(protoDf))

# plot the dataframe latlong with pyplot
def plotLatLongScatter(df):
    df.plot.scatter(x='lat', y='long')
    plt.show()

'''
df = makeDataFrame(locations)

print('total number of items:')
print(len(df.index))

df2 = df[(df['accuracy'] > 20) & (df['accuracy'] < 100)]
print(len(df2.index))

from sklearn.cluster import KMeans

latlong = []
for index, row in df2.iterrows():
    latlong.append([row['lat'],row['long']])
'''

# do clustering with regards to the whole
def clusterLatLongs(n):
    # Make Nx2 array with lat and long columns
    #X = np.array(makeLatLongArray(locations))
    X = makeDataFrame(locations)[['lat', 'long']]

    # initialize a KMeans klustering
    kmeans = KMeans(n_clusters=n)
    # Apply the KMeans to the data
    kmeans.fit(X)

    # Print the centroids
    print(kmeans.cluster_centers_)

    # there are labels from 
    X['cluster'] = kmeans.labels_

    print('Total number of items: ' + str(len(X.index)))

    print(len(denmark))
    # Plot the clusterings
    plt.scatter(X['long'],X['lat'], c=X['cluster'])
    plt.show()

clusterLatLongs(4)