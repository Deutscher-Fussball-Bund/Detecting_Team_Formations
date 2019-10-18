import sys
# Add the main folder path to the sys.path list
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
            
RAW_DATA = os.path.dirname(__file__) + '/../Data_STS/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml'
#FIRST_FRAME=10000
NUMBER_OF_FRAMES_TO_USE=30000 #77663 <- Erste Halbzeit Ende
# 118452 <- Zweite Halbzeit Ende Wechsel
# 100001
# 173675 <- Zweite Halbzeit Ende
# 173675

event_data = RawEventDataReader(RAW_DATA)
player_columns=["X","Y","D","A","S","M","T","N"]


x_pos=[]
y_pos=[]
p_id=[]
players=[]
for frameset in event_data.xml_root.iter('FrameSet'):
    if frameset.get('GameSection') != 'firstHalf':continue
    if frameset.get('TeamId') != 'DFL-CLU-000N99':continue
    if frameset.get('PersonId') != 'DFL-OBJ-0000I4':continue

    #    
    print(frameset)

    print(frameset.get('PersonId'))
    player_df = event_data.create_player_dataframe(player_columns, frameset.get('PersonId')) # 1. + 2. Halbzeit werden zusammengefasst
    FIRST_FRAME = player_df['N'][0]
    LAST_FRAME = player_df['N'].iloc[-1]

    #
    print(FIRST_FRAME)
    print(LAST_FRAME)
    print(Player(player_df, FIRST_FRAME).meanFL('X', FIRST_FRAME, 77663))
    print(Player(player_df, FIRST_FRAME).meanFL('X', 100001, 173675))
    
    

    p_id = (frameset.get('PersonId'))
    x_vals = []
    y_vals = []
    #for i in tqdm(range(0,NUMBER_OF_FRAMES_TO_USE)):
     #   x_vals.append(Player(player_df,FIRST_FRAME+i).X)
      #  y_vals.append(Player(player_df,FIRST_FRAME+i).Y)
    #x_pos = np.mean(x_vals)
    #y_pos = np.mean(y_vals)
    print(1, x_pos, y_pos)
    # for i in tqdm(range(0,NUMBER_OF_FRAMES_TO_USE)):
    #PlayerStatus= Player(player_df,FIRST_FRAME+i).BallStatus
    #if PlayerStatus==0:continue

        # x = Player(player_df,FIRST_FRAME+i).X
        # y = Player(player_df,FIRST_FRAME+i).Y
        #speed= Player(player_df,FIRST_FRAME+i).S

        # x_pos.append(x)
        # y_pos.append(y)

    x_pos = player_df['X'].mean()
    y_pos = player_df['Y'].mean()
    print(2, x_pos, y_pos)
    print(player_df['X'])
    x_vals = []
    y_vals = []
    77663
    #for i in tqdm(range(int(FIRST_FRAME), 141337)):
    #    x_vals.append(player_df['X'][i])
    #    y_vals.append(player_df['Y'][i])
    x_pos = np.mean(x_vals)
    y_pos = np.mean(y_vals)
    print(3, x_pos, y_pos)

    players.append([p_id, (x_pos, y_pos)])

Pitch("#195905", "#faf0e6")
for player in players:
    plt.annotate(player[0], xy=player[1], zorder=10)
plt.show()
quit()

Pitch("#195905","#faf0e6")
heatmap, xedges, yedges = np.histogram2d(x_pos, y_pos, bins=(105,68))
extent = [-52.5,52.5,-34,34]
plt.imshow(heatmap.T,cmap='rainbow',origin="lower", extent=extent,interpolation='bilinear',zorder=12,alpha=0.65)
plt.show()