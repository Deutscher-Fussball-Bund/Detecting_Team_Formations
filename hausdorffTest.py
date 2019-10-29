import numpy as np
from hausdorff import hausdorff_distance
import itertools

#test=list(itertools.permutations([[[3],[4]],[[8],[3]],[[18],[-3]],[[6],[13]],[[45],[-2]]]))
#for i in test:
#    print(i)
#print(len(test))
#print(test[0])              #([[3], [4]], [[8], [3]], [[18], [-3]], [[6], [13]], [[45], [-2]])
#print(test[0][0])           #[[3], [4]]
#print(test[0][0][0])        #[3]
#print(test[0][0][0][0])     #3

#quit()

# two random 2D arrays (second dimension must match)
X = [[[-7.227071057192374, 11.636347153712839, 15.136372483668845], [-0.8406439141447805, -4.224595387281696, -1.0495080655912536]], [[-45.527506999066794, -42.679281429142776, -34.491425143314224], [-0.2882548993467538, 0.12908412211705106, 0.33933608852153024]], [[-18.325539261431807, 3.391519797360353, 0.6650313291561127], [-19.775515264631384, -20.44903479536062, -17.997301693107588]]]
Y = []

# 3 vorgegebene Formationen
y = [[[1,2,3],[4,5,6]],[[2,3,1],[5,6,4]],[[1,2,3],[4,5,6]]]
# [x1,x2,...,xn],[y1,y2,...,yn] von n Spieler
x = [[7,6,8],[1,2,3]]

x=[[[3],[4]],[[18],[-3]],[[6],[13]],[[8],[3]],[[45],[-2]]]
y=[[[[13],[4]],[[-4],[0]],[[11],[3]],[[28],[5]],[[34],[5]]] , [[[23],[4]],[[2],[25]],[[3],[-2]],[[11],[23]],[[14],[15]]]]
#x=np.array(x)
y=np.array(y)

max_distance=0
for formation in y:
    max_formation=0
    formation=formation.transpose(2,0,1).reshape(10,-1)
    permutations=list(itertools.permutations(x))
    for permutation in permutations:
        # np.arrays müssen noch in richtige Form gebracht werden
        # np macht 2-dimensionale Arrays zu 3-dimensionalen Arrays
        permutation=np.array(permutation).transpose(2,0,1).reshape(10,-1)
        hd=hausdorff_distance(permutation, formation, distance="euclidean")
        print(hd)
    #for player in x:
    #    print("Hausdorff distance test: {0}".format( hausdorff_distance(player, formation, distance="euclidean"))) #manhatten,chebshev,cosine