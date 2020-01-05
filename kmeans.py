from sklearn.cluster import KMeans
import numpy as np


def calculate_cluster(formations, n_clusters):
    print('np array wird erstellt.')
    X = np.array(formations)
    print('shaping')
    nsamples, nx, ny = X.shape
    print(nsamples,nx,ny)
    d2_train_dataset = X.reshape((nsamples,nx*ny))
    print('fitting')
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(d2_train_dataset)
    #print(kmeans.labels_)
    #kmeans.predict([[0, 0], [12, 3]])
    #print(kmeans.cluster_centers_)
    return create_3d_array(kmeans.cluster_centers_)

def create_3d_array(array):
    formations=[]
    for team in array:
        formation=[]
        i=0
        while i<len(team):
            formation.append([team[i],team[i+1]])
            i+=2
        formations.append(formation)
    return formations