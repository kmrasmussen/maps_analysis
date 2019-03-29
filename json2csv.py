import json
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

dataframe = makeDataFrame(getLocationList())
dataframe.to_csv('dataset.csv')
