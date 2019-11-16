import numpy as np
from hausdorff import hausdorff_distance
import itertools

#x=[[[3],[4]],[[18],[-3]],[[6],[13]],[[8],[3]],[[45],[-2]]]
#x=[[3,4],[18,-3],[6,13],[8,3],[45,-2]]
#y=[[[[13],[4]],[[-4],[0]],[[11],[3]],[[28],[5]],[[34],[5]]] , [[[23],[4]],[[2],[25]],[[3],[-2]],[[11],[23]],[[14],[15]]]]
#print(0,x)
#x=np.array(x)
#print(1,x)
#y=np.array(y)

#max_distance=0
#for formation in y:
#    max_formation=0
#   formation=formation.transpose(2,0,1).reshape(10,-1)
#    team=x.reshape(10,-1)
#    print(4,x)
    
#    hd=hausdorff_distance(team, formation, distance="euclidean")
#    print(hd)
    #for player in x:
    #    print("Hausdorff distance test: {0}".format( hausdorff_distance(player, formation, distance="euclidean"))) #manhatten,chebshev,cosine

def get_hausdorff(team1, team2):
    team1 = np.array(team1).reshape(10,-1)
    team2 = np.array(team2).reshape(10,-1)
    hd=hausdorff_distance(team1, team2, distance="euclidean")
    return hd