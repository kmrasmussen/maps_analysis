# data set is stored as json
import json
# easy to make csv with pandas
import pandas as pd

def getLocationList():
    # open the file
    locationFile = open('dataset.json')
    # get the contents of the file
    fileContent = locationFile.read().replace('\n','')
    # parse the json. There is only one element in the object, namely locations
    locations = json.loads(fileContent)['locations']
    return(locations)

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

# elements in list may differ, some have special properties.
# They all seem to have timestampMs, longitude, latitude and accuracy
def printSimpleStats(locations):
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

locations = getLocationList()
dataframe = makeDataFrame(locations)
dataframe.to_csv('dataset.csv')
printSimpleStats(locations)
