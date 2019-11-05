import os
from tacticon.Pitch import Pitch
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from avg_formation import get_avg_formations
import random

playerPositions = get_avg_formations(os.path.dirname(__file__) + '/../Data_STS/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml', 50000, 101000, 'DFL-CLU-000N99')
print(playerPositions) #zweiteHalbzeit.xml
Pitch("#195905", "#faf0e6")
for positions in playerPositions:
    plt.scatter(positions[0], positions[1], c=range(0, len(positions[0])), cmap='rainbow', zorder=10)
    plt.annotate(random.randrange(11), (positions[0][0],positions[1][0]), textcoords="offset points", xytext=(0,10), ha='center')
plt.show()

quit()

F532 = [[-25,20], [-30,10], [-30,0], [-30,-10], [-25,-20], [-20,5], [-20,-5], [-5,5], [0,0], [-5,-5]]
F442R= [[-25,15], [-30,5], [-30,-5], [-25,-15], [-15,15], [-20,0], [-10,0], [-15,-15], [-5,5], [-5,-5]]

x_pos=[]
y_pos=[]
playerPositions=[]
for player in F532:
    x_pos.append(player[0])
    y_pos.append(player[1])
playerPositions.append([x_pos,y_pos,'red'])
x_pos=[]
y_pos=[]
for player in F442R:
    x_pos.append(player[0])
    y_pos.append(player[1])
playerPositions.append([x_pos,y_pos,'blue'])

#print(playerPositions)

for positions in playerPositions:
    #print(len(positions[0]))
    #print(positions)
    Pitch("#195905", "#faf0e6")
    plt.scatter(positions[0], positions[1], c=positions[2], zorder=10)
    plt.show()

quit()

x_pos=[1,2,3,4,5,6,7,8,9,10]
y_pos=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
playerPositions=[[x_pos, y_pos]]
x_pos=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y_pos=[1,2,3,4,5,6,7,8,9,10]
playerPositions.append([x_pos, y_pos])
x_pos=[1,2,3,4,5,6,7,8,9,10]
y_pos=[1,2,3,4,5,6,7,8,9,10]
playerPositions.append([x_pos, y_pos])
x_pos=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y_pos=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
playerPositions.append([x_pos, y_pos])


print(playerPositions)
Pitch("#195905", "#faf0e6")
for positions in playerPositions:
    print(positions)
    print(positions[0])
    plt.scatter(positions[0], positions[1], c=range(0, len(positions[0])), cmap='rainbow', zorder=10)
plt.show()