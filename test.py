import os
import numpy as np

from start_analysis import start_analysis
from avg_formation import get_gks
from Team import create_team_df


"""
Halbzeit 1 beginnt bei:
10002.0
und endet bei:
77663.0
Halbzeit 2 beginnt bei:
100001.0
und endet bei:
173675.0

DFL-OBJ-0000ZS
157872.0
173675.0
DFL-OBJ-0000O3
122801.0
173675.0
DFL-OBJ-00021U
122556.0
173675.0
DFL-OBJ-0027GH
10002.0
122555.0
DFL-OBJ-0000OJ
10002.0
122800.0
DFL-OBJ-000280
10002.0
157871.0
"""

def get_substitutions(team_df, halftime):
    #Auswechslung erkennen
    substitutions = {}
    for player in team_df.columns:
        if team_df[player].isnull().values.any():
            print(player)
            print(team_df[team_df[player].isnull()].index[0])
            print(team_df[team_df[player].isnull()].index[-1])
            #print(team_df[team_df[player].isnull()])
            #quit()
            if team_df[team_df[player].isnull()].index[0]==halftime[0]:
                if team_df[team_df[player].isnull()].index[-1] not in substitutions.keys():
                    substitutions[team_df[team_df[player].isnull()].index[-1]] = {}
                substitutions[team_df[team_df[player].isnull()].index[-1]]['on'] = player[0]
            if team_df[team_df[player].isnull()].index[-1]==halftime[3]:
                if team_df[team_df[player].isnull()].index[0]-1 not in substitutions.keys():
                    substitutions[team_df[team_df[player].isnull()].index[0]-1] = {}
                substitutions[team_df[team_df[player].isnull()].index[0]-1]['off'] = player[0]        
    return substitutions

def get_halftime(team_df):
    """
    Gibt den ersten und letzten Frame einer Halbzeit zurück.
    """
    halftime=[]
    for half in team_df.groupby(team_df.index.to_series().diff().ne(1).cumsum()).groups:
        halftime.append(team_df.groupby(team_df.index.to_series().diff().ne(1).cumsum()).groups[half][0])
        halftime.append(team_df.groupby(team_df.index.to_series().diff().ne(1).cumsum()).groups[half][-1])
    return halftime

def get_formation(team_df,ff,lf):
    k=0
    formation=[]
    while k<len(team_df[ff:lf].mean(skipna = True)):
        if np.isnan(team_df.loc[ff][k]):
            k+=2
            continue
        formation.append([round(team_df[ff:lf].mean(skipna = True)[k],2),round(team_df[ff:lf].mean(skipna = True)[k+1],2)])
        k+=2
    print(formation)


def make_intervalls(team_df,frames,halftimes,substitutions):
    i = halftime[0]
    while i<halftime[1]:
        j=i+frames
        if j>halftime[1]:j=halftime[1]
        print('')
        for substitution in substitutions:
            if substitution>i and substitution<j:
                print('Auswechslung nach Zeitintervall')
                j=substitution
        
        print(i,j)
        get_formation(team_df,i,j)
        i=j+1
    
    i = halftime[2]
    while i<halftime[3]:
        j=i+frames
        if j>halftime[3]:j=halftime[3]
        print('')
        for substitution in substitutions:
            if substitution>i and substitution<j:
                print('Auswechslung nach Zeitintervall')
                j=substitution
        
        print(i,j)
        get_formation(team_df,i,j)
        i=j+1
    


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
make_intervalls(team_df,10000,halftime,substitutions)





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