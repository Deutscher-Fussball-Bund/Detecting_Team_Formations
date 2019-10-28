import numpy as np
from hausdorff import hausdorff_distance

# two random 2D arrays (second dimension must match)
X = [[[-7.227071057192374, 11.636347153712839, 15.136372483668845], [-0.8406439141447805, -4.224595387281696, -1.0495080655912536]], [[-45.527506999066794, -42.679281429142776, -34.491425143314224], [-0.2882548993467538, 0.12908412211705106, 0.33933608852153024]], [[-18.325539261431807, 3.391519797360353, 0.6650313291561127], [-19.775515264631384, -20.44903479536062, -17.997301693107588]]]
Y = []

# 3 vorgegebene Formationen
y = [[[1,2,3],[4,5,6]],[[2,3,1],[5,6,4]],[[1,2,3],[4,5,6]]]
# [x1,x2,...,xn],[y1,y2,...,yn] von n Spieler
x = [[7,6,8],[1,2,3]]
x=np.array(x)
y=np.array(y)

for formation in y:
    print(formation)
    # Test computation of Hausdorff distance with different base distances
    #print("Hausdorff distance test: {0}".format( hausdorff_distance(player, y, distance="manhattan") ))
    print("Hausdorff distance test: {0}".format( hausdorff_distance(x, formation, distance="euclidean") ))
    #print("Hausdorff distance test: {0}".format( hausdorff_distance(player, y, distance="chebyshev") ))
    #print("Hausdorff distance test: {0}".format( hausdorff_distance(player, y, distance="cosine") ))