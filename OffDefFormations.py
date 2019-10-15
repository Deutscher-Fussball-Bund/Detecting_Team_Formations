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
NUMBER_OF_FRAMES_TO_USE=15000 #77663

event_data = RawEventDataReader(RAW_DATA)
player_columns=["X","Y","D","A","S","M","T","N"]
player_df = event_data.create_player_dataframe(player_columns, 'DFL-OBJ-0002F5')

FIRST_FRAME = player_df['N'][0]

print(FIRST_FRAME)

x_pos=[]
y_pos=[]
for i in tqdm(range(0,NUMBER_OF_FRAMES_TO_USE)):
    #PlayerStatus= Player(player_df,FIRST_FRAME+i).BallStatus
    #if PlayerStatus==0:continue

    x= Player(player_df,FIRST_FRAME+i).X
    y= Player(player_df,FIRST_FRAME+i).Y
    #speed= Player(player_df,FIRST_FRAME+i).S

    x_pos.append(x)
    y_pos.append(y)

Pitch("#195905","#faf0e6")
heatmap, xedges, yedges = np.histogram2d(x_pos, y_pos, bins=(105,68))
extent = [-52.5,52.5,-34,34]
plt.imshow(heatmap.T,cmap='rainbow',origin="lower", extent=extent,interpolation='bilinear',zorder=12,alpha=0.65)
plt.show()