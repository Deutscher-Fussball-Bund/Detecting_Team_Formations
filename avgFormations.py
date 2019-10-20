import sys
sys.path.append('../')
from tacticon.RawEventDataReader import RawEventDataReader
from tacticon.Player import Player
from tacticon.Pitch import Pitch
from tacticon.Team import Team
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np
import os
import matplotlib.cm as cm


RAW_DATA = os.path.dirname(__file__) + '/../Data_STS/ersteHalbzeit.xml'
event_data = RawEventDataReader(RAW_DATA)
player_columns=["X","Y","D","A","S","M","T","N"]


playerPositions=[]
for frameset in event_data.xml_root.iter('FrameSet'):
    if frameset.get('GameSection') != 'firstHalf':continue
    if frameset.get('TeamId') != 'DFL-CLU-000N99':continue
    #if frameset.get('PersonId') != 'DFL-OBJ-0000I4':continue
    print(frameset.get('PersonId'))

   
    player_df = event_data.create_player_dataframe(player_columns, frameset.get('PersonId'))

    for i in range(10002,77663,7500):
        x_pos,y_pos=[],[]
        j = i + 7500
        if j > 77663: j = 77663
        #print(i, j)

        x_pos.append(Player(player_df, i).meanFL('X', i, j))
        y_pos.append(Player(player_df, i).meanFL('Y', i, j))
        playerPositions.append([x_pos, y_pos])

print(playerPositions)
pos=[]
for i in range(len(playerPositions[0][0])):
    x,y = [],[]
    print(i)
    for player in playerPositions:
        x.append(player[0][i])
        y.append(player[1][i])
    pos.append([x,y])
print(pos)

Pitch("#195905", "#faf0e6")
for positions in pos:
    plt.scatter(positions[0], positions[1], c=range(0, len(playerPositions)), cmap='rainbow', zorder=10)
plt.show()



quit()

#FIRST_FRAME=10000
NUMBER_OF_FRAMES_TO_USE=30000 #77663 <- Erste Halbzeit Ende
# 118452 <- Zweite Halbzeit Ende Wechsel
# 100001
# 173675 <- Zweite Halbzeit Ende
# 173675
