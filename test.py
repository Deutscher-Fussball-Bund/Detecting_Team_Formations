
from tacticon.Pitch import Pitch
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt

F532 = [[-25,30], [-30,20], [-30,0], [-30,-20], [-25,-30], [-15,10], [-15,-10], [5,5], [10,0], [5,-5]]
F442R= [[-25,25], [-30,10], [-30,-10], [-25,-25], [-10,25], [-15,0], [-5,0], [-10,-25], [5,5], [5,-5]]
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