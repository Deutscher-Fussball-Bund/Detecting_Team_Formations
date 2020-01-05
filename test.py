import os
import numpy as np
import pandas as pd

from start_analysis import start_analysis,start_clustering_matches
#from avg_formation import get_gks
from team import create_team_df

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from tacticon.Pitch import Pitch
from formations import get_formations

from tacticon.RawEventDataReader import RawEventDataReader
from matchinformation import get_gks
from kmeans import calculate_cluster

info_path_GER_EST=os.path.dirname(__file__) + '/../Daten/GER_EST/DFL_02_01_matchinformation_DFL-COM-000001_DFL-MAT-003BEU (1).xml'
path_GER_EST=os.path.dirname(__file__) + '/../Daten/GER_EST/DFL_04_03_positions_raw_observed_DFL-COM-000001_DFL-MAT-003BEU.xml'

info_path_GER_NL=os.path.dirname(__file__) + '/../Daten/GER_NL/DFL_02_01_matchinformation_DFL-COM-000001_DFL-MAT-X03BWS.xml' #'DFL-CLU-000N9A')#DFL-CLU-000N99
path_GER_NL=os.path.dirname(__file__) + '/../Daten/GER_NL/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml'

info_path_GER_BEL_U21=os.path.dirname(__file__) + '/../Daten/GER_BEL_U21/DFL_02_01_matchinformation_DFL-COM-000001_DFL-MAT-003BWT.xml'
path_GER_BEL_U21=os.path.dirname(__file__) + '/../Daten/GER_BEL_U21/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-003BWT.xml'

info_path_GER_NIR=os.path.dirname(__file__) + '/../Daten/GER_NIR/DFL_02_01_matchinformation_DFL-COM-000001_DFL-MAT-003BWS.xml'
path_GER_NIR=os.path.dirname(__file__) + '/../Daten/GER_NIR/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-003BWS.xml'



matches=[[path_GER_EST,info_path_GER_EST],[path_GER_NL,info_path_GER_NL],[path_GER_NIR,info_path_GER_NIR],[path_GER_BEL_U21,info_path_GER_BEL_U21]]

cluster=start_clustering_matches(matches)
print('')
i=1
for formation in cluster:
    Pitch("#195905", "#faf0e6")
    for player in formation:
        plt.scatter(player[0], player[1], c='red', zorder=10)
        #plt.title(formation)
    plt.show()
    plt.savefig('Figure_'+str(i)+'.png')
    i+=1


quit()

formations=[[[-1.27, -4.56], [14.39, 22.18], [21.82, -13.35], [21.4, 10.16], [11.15, 4.8], [22.03, -3.36], [14.59, -6.36], [-0.5, 11.33], [12.05, 14.67], [5.36, -11.67]], [[-1.74, -2.03], [10.64, 25.32], [22.36, -11.77], [21.23, 13.73], [10.31, 8.3], [22.42, -1.13], [14.53, -3.02], [-1.5, 15.84], [11.49, 17.83], [5.43, -9.41]], [[-2.75, 0.08], [6.53, 26.96], [22.0, -10.64], [20.29, 15.97], [7.82, 10.65], [21.49, 0.57], [13.85, -0.11], [-3.66, 18.96], [10.09, 19.62], [4.57, -7.63]], [[-4.75, 1.6], [3.68, 27.06], [20.44, -10.12], [18.65, 16.18], [3.9, 11.51], [19.5, 1.15], [12.3, 1.79], [-6.23, 19.91], [7.95, 19.71], [2.68, -7.0]], [[-7.87, 2.64], [2.92, 26.51], [18.5, -10.35], [16.65, 14.88], [-0.16, 11.29], [17.42, 0.34], [10.14, 2.45], [-8.27, 19.03], [5.33, 18.47], [0.14, -7.6]], [[-11.36, 4.02], [3.28, 26.16], [16.91, -11.04], [14.43, 13.81], [-3.11, 11.15], [15.64, -0.83], [7.99, 2.54], [-9.8, 18.02], [2.84, 17.35], [-2.29, -8.5]], [[-14.41, 6.06], [2.91, 26.58], [15.61, -11.44], [12.52, 14.03], [-4.78, 11.8],[13.98, -1.24], [6.35, 3.03], [-11.56, 18.63], [0.79, 17.65], [-4.17, -8.52]], [[-16.67, 8.28], [1.06, 27.91], [14.07, -10.84], [11.52, 15.92], [-5.32, 13.34], [12.58, -0.05], [5.37, 4.25], [-13.53, 21.41], [-0.59, 19.74], [-5.42, -7.32]], [[-17.9, 9.66], [-0.78, 29.54], [12.81, -9.23], [11.85, 18.85], [-4.8, 15.13], [12.78, 2.82], [5.24, 5.83], [-14.53, 25.19], [-0.47, 22.92], [-6.03, -5.44]], [[-17.93, 10.11], [-0.79, 30.64], [12.84, -7.41], [13.27, 22.51], [-2.96, 16.86], [14.93, 7.01], [6.06, 7.24], [-13.64, 28.47], [1.58, 25.77], [-6.08, -3.55]], [[-16.81, 10.13], [1.53, 30.76], [14.2, -6.04], [15.32, 25.58], [-0.02, 18.35], [17.96, 11.67], [7.61, 8.24], [-11.25, 30.35], [5.22, 27.47], [-5.67, -1.99]], [[-15.21, 10.07], [4.72, 30.43], [16.02, -5.32], [17.78, 27.39], [3.07, 19.78], [19.91, 15.41], [9.33, 8.98], [-8.43, 31.1], [9.38, 27.51], [-4.96, -0.79]], [[-13.55, 9.96], [7.63, 30.29], [17.56, -4.92], [20.54,27.77], [5.96, 20.87], [20.5, 17.25], [10.9, 9.58], [-5.99, 31.41], [13.4, 26.65], [-4.05, 0.14]], [[-11.88, 9.73], [9.96, 30.78], [18.86, -4.66], [23.3, 27.53], [8.63, 21.28], [21.09, 17.13], [12.39, 10.06], [-4.03, 31.65], [16.59, 25.45], [-3.02, 0.88]], [[-10.25, 9.41], [11.81, 31.3], [20.03, -4.77], [25.59, 27.36], [11.31, 20.58], [22.83, 15.68], [13.89, 10.0], [-2.41, 31.74], [18.55, 24.32], [-1.89, 1.19]], [[-8.65, 9.0], [13.35, 31.43], [20.89, -5.36], [27.37, 26.91], [13.88, 19.05], [25.48, 13.49], [15.18, 9.09], [-0.96, 31.54], [19.11, 23.2], [-0.87, 0.91]]]
cluster=calculate_cluster(formations,2)
print(cluster)
for formation in cluster:
    Pitch("#195905", "#faf0e6")
    for player in formation:
        plt.scatter(player[0], player[1], c='red', zorder=10)
        #plt.title(formation)
    plt.show() 
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