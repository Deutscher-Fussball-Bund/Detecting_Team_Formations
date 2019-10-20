import sys
sys.path.append('../')
from Detecting_Team_Formations.tacticon.RawEventDataReader import RawEventDataReader
from Detecting_Team_Formations.tacticon.Player import Player
from Detecting_Team_Formations.tacticon.Pitch import Pitch
from Detecting_Team_Formations.tacticon.Team import Team
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

### Erste Halbzeit
x_posF, x_posS =[], []
y_posF, y_posS =[], []
p_id =[]
playersF, playersS =[], []
for frameset in event_data.xml_root.iter('FrameSet'):
    if frameset.get('GameSection') != 'firstHalf':continue
    if frameset.get('TeamId') != 'DFL-CLU-000N99':continue
    #if frameset.get('PersonId') != 'DFL-OBJ-0000I4':continue

    print(frameset.get('PersonId'))
    player_df = event_data.create_player_dataframe(player_columns, frameset.get('PersonId')) # 1. + 2. Halbzeit werden zusammengefasst
    FIRST_FRAME = player_df['N'][0]
    LAST_FRAME = player_df['N'].iloc[-1]

    p_id.append(frameset.get('PersonId'))
    x_posF.append(Player(player_df, FIRST_FRAME).meanFL('X', FIRST_FRAME, 77663))
    y_posF.append(Player(player_df, FIRST_FRAME).meanFL('Y', FIRST_FRAME, 77663))  
    x_posS.append(Player(player_df, FIRST_FRAME).meanFL('X', 100001, LAST_FRAME))
    y_posS.append(Player(player_df, FIRST_FRAME).meanFL('Y', 100001, LAST_FRAME))
    
    playersF.append([p_id, x_posF, y_posF])
    playersS.append([p_id, x_posS, y_posS])

Pitch("#195905", "#faf0e6")
for player in playersF:
    plt.scatter(player[1], player[2], zorder=10)
plt.show()

Pitch("#195905", "#faf0e6")
for player in playersS:
    plt.scatter(player[1], player[2], zorder=10)
plt.show()