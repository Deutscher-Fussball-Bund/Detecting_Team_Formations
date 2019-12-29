import numpy as np

def get_substitutions(team_df, halftime):
    #Auswechslung erkennen
    substitutions = {}
    for player in team_df.columns:
        player_isnull=team_df[player].isnull()
        if player_isnull.values.any():
            if team_df[player_isnull].index[0]==halftime[0]:
                if team_df[player_isnull].index[-1] not in substitutions.keys():
                    substitutions[team_df[player_isnull].index[-1]] = {}
                substitutions[team_df[player_isnull].index[-1]]['on'] = player[0]
            if team_df[player_isnull].index[-1]==halftime[3]:
                if team_df[player_isnull].index[0]-1 not in substitutions.keys():
                    substitutions[team_df[player_isnull].index[0]-1] = {}
                substitutions[team_df[player_isnull].index[0]-1]['off'] = player[0]        
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

def get_formation(team_df,ff,lf,invert):
    k=0
    formation=[]
    while k<len(team_df[ff:lf].mean(skipna = True)):
        if np.isnan(team_df.loc[ff][k]):
            k+=2
            continue
        formation.append([round(team_df[ff:lf].mean(skipna = True)[k],2)*invert,round(team_df[ff:lf].mean(skipna = True)[k+1],2)*invert])
        k+=2
    return formation

def get_avg_formations(team_df,frames):
    halftimes=get_halftime(team_df)
    substitutions=get_substitutions(team_df,halftimes)
    formations=[]
    i = halftimes[0]
    while i<halftimes[1]:
        j=i+frames
        if j>halftimes[1]:j=halftimes[1]
        for substitution in substitutions:
            if substitution>i and substitution<j:
                j=substitution
        
        formations.append(get_formation(team_df,i,j,1))
        i=j+1
    
    i = halftimes[2]
    while i<halftimes[3]:
        j=i+frames
        if j>halftimes[3]:j=halftimes[3]
        for substitution in substitutions:
            if substitution>i and substitution<j:
                j=substitution
        
        formations.append(get_formation(team_df,i,j,-1))
        i=j+1
    
    return formations