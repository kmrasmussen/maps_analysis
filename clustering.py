import pandas as pd
import matplotlib.pyplot as plt
# clustering using KMeans
from sklearn.cluster import KMeans

# do clustering with regards to the whole
def clusterLatLongs(n, df):
    # Make Nx2 array with lat and long columns
    #X = np.array(makeLatLongArray(locations))
    X = df[['lat', 'long']]

    print('')
    # initialize a KMeans klustering
    kmeans = KMeans(n_clusters=n)
    # Apply the KMeans to the data
    print('Fitting data...')
    kmeans.fit(X)

    print(str(n) + ' geographical centroids:')
    # Print the centroids
    print(kmeans.cluster_centers_)

    print('Making cluster row in dataframe')
    # there are labels from 
    df['cluster'] = kmeans.labels_
    return(df)

def plotClusters(X):
    print('Total number of items: ' + str(len(X)))
    # Plot the clusterings
    print('Plotting with pyplot')
    plt.scatter(X['long'],X['lat'], c=X['cluster'])
    
def savePlot(plotFileName):
    print('Saving plot as ' + plotFileName)
    plt.savefig(plotFileName)
    print('Saved image as latlongCluster.png')

K = 4
plotFileName = 'latlongClusters.png'
print('KMeans clustering of latlong with K = ' + str(K))

print('Reading dataset.csv')
df = pd.read_csv('dataset.csv')

df = clusterLatLongs(K, df)

print('Plotting')
plotClusters(df)
print('Saving png')
savePlot(plotFileName)