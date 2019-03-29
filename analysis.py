
import numpy as np
import pandas as pd
import datetime

# plot the dataframe latlong with pyplot
def plotLatLongScatter(df):
    df.plot.scatter(x='lat', y='long')
    plt.show()


def unixmsToDateTime(unixMiliseconds): 
    # convert to standard Unixdate time int
    timestamp = unixMiliseconds // 1000
    # use Python datetime
    result = datetime.datetime.fromtimestamp(timestamp)
    return(result)

def DateTimeToDateString(time):
    encoded = str(x.year) + str(x.month) + str(x.day)
    return(encoded)

def lookDaysFromTime(current):
    for i in range(10):
        print(current)
        current = current + datetime.timedelta(days=1)

df = pd.read_csv('maps.csv')

for i in range(1,10):
    print(df.iloc[0])
    tminus1 = df.iloc[i-1]['time']
    t = df.iloc[i]['time']
    deltat = t - tminus1
    print(deltat)

#df['datetime'] = unixmsToDateTime(df['time'])

#print(df.head())

#int(df.iloc[0]['time'])


