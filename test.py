import os
import numpy as np
import pandas as pd

from start_analysis import start_analysis,start_clustering
#from avg_formation import get_gks
from team import create_team_df

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from tacticon.Pitch import Pitch
from formations import get_formations

from tacticon.RawEventDataReader import RawEventDataReader

ball_col=["N","BallPossession","BallStatus"]
'19-06-12_Mainz_GER_EST Sportec Data/DFL_04_03_positions_raw_observed_DFL-COM-000001_DFL-MAT-003BEU.xml'  #DFL-CLU-000N8Y
'Data_STS/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml' #DFL-CLU-000N99
event_data = RawEventDataReader(os.path.dirname(__file__) + '/../19-06-12_Mainz_GER_EST Sportec Data/DFL_04_03_positions_raw_observed_DFL-COM-000001_DFL-MAT-003BEU.xml')
df=start_clustering(os.path.dirname(__file__) + '/../19-06-12_Mainz_GER_EST Sportec Data/DFL_04_03_positions_raw_observed_DFL-COM-000001_DFL-MAT-003BEU.xml','DFL-CLU-000N8Y')

print(df)




quit()

start_analysis(os.path.dirname(__file__) + '/../Data_STS/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml',30,'DFL-CLU-000N99')

quit()

formations=get_formations()
for formation in formations:
    Pitch("#195905", "#faf0e6")
    for player in formations[formation]:
        plt.scatter(player[0], player[1], c='red', zorder=10)
        plt.title(formation)
    plt.show()  

quit()


team_df = create_team_df(os.path.dirname(__file__) + '/../Data_STS/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml', 'DFL-CLU-000N99')
#'/../Data_STS/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml', 'DFL-CLU-000N99')
#start_analysis(os.path.dirname(__file__) + '/../Data_STS/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml', 180, 'DFL-CLU-000N99')
#print('')
print('Torhüter werden entfernt.')
path=os.path.dirname(__file__) + '/../Data_STS/DFL_01_05_masterdata_DFL-CLU-000N99_DFL-SEA-0001K4_player.xml'
gk_ids = get_gks(path)
for gk in gk_ids:
    if gk in team_df.columns:
        team_df.drop(columns=[gk], level=0, inplace=True)

#print('')
#print('')
#print('')

#print(team_df.loc[122555.0])
#print(team_df.loc[122556.0])
#print(team_df.loc[122557.0])
#quit()

halftime=get_halftime(team_df)
substitutions=get_substitutions(team_df,halftime)
formations=make_intervalls(team_df,25000,halftime,substitutions)

for formation in formations:
    print('')
    Pitch("#195905", "#faf0e6")
    for player in formation:
        print(player)
        
        plt.scatter(player[0], player[1], c='red', zorder=10)
    plt.show()


quit()

# [[23,34],[344,45],..]

print('')
print('')

print(team_df[10003.0:10007.0])

print('')
print('')

print(team_df[10003.0:10007.0].mean())

print('')
for val in team_df[10003.0:10007.0].mean(skipna = True):
    print(val)
print('')

print('')
i=0
while i<len(team_df[10003.0:10007.0].mean(skipna = True)):
    print(team_df[10003.0:10007.0].mean(skipna = True)[i],team_df[10003.0:10007.0].mean(skipna = True)[i+1])
    i+=2
print('')
#isnull().values.any()

    

quit()
"""
arrays1 = [['Neuer', 'Neuer', 'Boateng', 'Boateng', 'Gnabry', 'Gnabry', 'Draxler', 'Draxler'],['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y']]
tuples1 = list(zip(*arrays1))
index1 = pd.MultiIndex.from_tuples(tuples1, names=['', ''])
df1 = pd.DataFrame(np.random.randn(3, 8), index=['10002', '10003', '10004'], columns=index1)
#print(df1)

arrays2 = [['Tah', 'Tah'],['X', 'Y']]
tuples2 = list(zip(*arrays2))
index2 = pd.MultiIndex.from_tuples(tuples2, names=['', ''])
df2 = pd.DataFrame(np.random.randn(2, 2), index=['10002', '10003'], columns=index2)
#print(df2)
df2 = pd.concat([df1, df2], axis=1, sort=False)
#print(df2)


arrays3 = [['Götze', 'Götze'],['X', 'Y']]
tuples3 = list(zip(*arrays3))
index3 = pd.MultiIndex.from_tuples(tuples3, names=['', ''])
df3 = pd.DataFrame(np.random.randn(1, 2), index=['10004'], columns=index3)
#print(df3)
df3 = pd.concat([df2, df3], axis=1, sort=False)
print(df3)


#print('')
#print(df3.loc[['10003']])
#print(df3.loc[['10003']]['Neuer'])
#print(df3.loc[['10003']]['Neuer']['X'])
#print('')
#print(df3['Tah'])
"""