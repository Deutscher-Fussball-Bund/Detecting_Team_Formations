import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import itertools

from hausdorff import hausdorff_distance
from tacticon.Pitch import Pitch
from array_operations import combine_xy, get_mean, move_formation
from formations import get_formations
    
#    hd=hausdorff_distance(team, formation, distance="euclidean")
#    print(hd)
    #for player in x:
    #    print("Hausdorff distance test: {0}".format( hausdorff_distance(player, formation, distance="euclidean"))) #manhatten,chebshev,cosine

def get_hausdorff(team1, team2):
    team1 = np.array(team1).reshape(10,-1)
    team2 = np.array(team2).reshape(10,-1)
    hd=hausdorff_distance(team1, team2, distance="euclidean")
    return hd

def calculate_formation(player_positions):
    Pitch("#195905", "#faf0e6")
    for i, positions in enumerate(player_positions):
        plt.scatter(positions[0], positions[1], c='red', zorder=10)
        #plt.annotate(shirtnumbers[i], (positions[0],positions[1]), textcoords="offset points", xytext=(0,10), ha='center')

    team_mean=get_mean(player_positions)
    plt.scatter(team_mean[0], team_mean[1], c='grey', zorder=10)
    plt.show()

    print('Standardformation wird geladen und verschoben.')
    formations = get_formations()
    formations_moved = move_formation(team_mean,formations)

    print('Hausdorff-Distanz wird berechnet.')
    hd_min=['test',100]
    for key in formations_moved:
        hd = get_hausdorff(player_positions,formations_moved[key])
        if(hd<hd_min[1]):
            hd_min=[key,hd]

    print('Ergebnis:', hd_min)

    Pitch("#195905", "#faf0e6")
    for positions in player_positions:
        plt.scatter(positions[0], positions[1], c='red', zorder=10)
    for positions in formations_moved[hd_min[0]]:
        plt.scatter(positions[0], positions[1], c='grey', zorder=10)
    plt.show()

def calculate_formations(player_positions):

    print(player_positions)
    quit()


    for formation in player_positions:
        team_mean=get_mean(player_positions)
        print('Standardformation wird geladen und verschoben.')
        formations = get_formations()
        formations_moved = move_formation(team_mean,formations)

        print('Hausdorff-Distanz wird berechnet.')
        hd_min=['test',100]
        for key in formations_moved:
            hd = get_hausdorff(player_positions,formations_moved[key])
            if(hd<hd_min[1]):
                hd_min=[key,hd]

        print('Ergebnis:', hd_min)