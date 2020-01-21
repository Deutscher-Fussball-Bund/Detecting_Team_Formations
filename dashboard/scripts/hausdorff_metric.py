import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import itertools

from hausdorff import hausdorff_distance

from dashboard.scripts.tacticon.Pitch import Pitch
from dashboard.scripts.array_operations import combine_xy, get_mean, move_formation
from dashboard.scripts.formations import get_formations
    
#    hd=hausdorff_distance(team, formation, distance="euclidean")
#    print(hd)
    #for player in x:
    #    print("Hausdorff distance test: {0}".format( hausdorff_distance(player, formation, distance="euclidean"))) #manhatten,chebshev,cosine

def get_hausdorff(team1, team2):
    team1 = np.array(team1).reshape(10,-1)
    team2 = np.array(team2).reshape(10,-1)
    hd=hausdorff_distance(team1, team2, distance="euclidean")
    return hd

def calculate_formation(formations):
    X = np.array(formations)
    nsamples,nx,ny = X.shape
    d2_dataset = X.reshape((nsamples,nx*ny))
    df = pd.DataFrame(data=d2_dataset)
    formation=[]
    for val in df.mean():
        formation.append(val)

    avg_formation=[]
    i=0
    while i<len(formation):
        avg_formation.append([formation[i],formation[i+1]])
        i+=2
    team_mean=get_mean(avg_formation)
   

    print('Standardformation wird geladen und verschoben.')
    formations = get_formations()
    formations_moved = move_formation(team_mean,formations)

    print('Hausdorff-Distanz wird berechnet.')
    hd_min=['default',100]
    for key in formations_moved:
        hd = get_hausdorff(avg_formation,formations_moved[key])
        if(hd<hd_min[1]):
            hd_min=[key,hd]

    print('Ergebnis:', hd_min)
    return avg_formation,hd_min

def calculate_formations(formations):
    hd_mins=[]
    print('Standardformation wird geladen und verschoben.')
    print('Hausdorff-Distanz wird berechnet.')
    for i, formation in enumerate(formations):
        team_mean=get_mean(formation)
        def_formations = get_formations()
        formations_moved = move_formation(team_mean,def_formations)
        
        hd_min=['default',100]
        for key in formations_moved:
            hd = get_hausdorff(formation,formations_moved[key])
            if(hd<hd_min[1]):
                hd_min=[key,hd]

        print('Ergebnis',i,':', hd_min)
        hd_mins.append(hd_min)
        #Pitch("#195905", "#faf0e6")
        #for player in formation:
        #    plt.scatter(player[0], player[1], c='red', zorder=10)
        #for positions in formations_moved[hd_min[0]]:
        #    plt.scatter(positions[0], positions[1], c='grey', zorder=10)
        #plt.show()
        #i+=1
    return hd_mins