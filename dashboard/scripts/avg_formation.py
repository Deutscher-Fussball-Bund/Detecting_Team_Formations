import numpy as np

from dashboard.scripts.matchinformation import get_gks

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

def cut_halftimes(halftimes,start_min,end_min):
    start=halftimes[0] + start_min*25*60
    end=halftimes[0] + (end_min+1)*25*60
    res=[]
    s=0
    if start_min==0:
        res.append(halftimes[0])
        if end_min==45:
            res.append(halftimes[1])
            return res,s
        if end_min<46:
            res.append(end)
            return res,s
        if end_min<90:
            res.append(halftimes[1])
            res.append(halftimes[2])
            res.append(end)
            return res,s
        else: return halftimes
    
    if start_min<46:
        res.append(start)
        if end_min==45:
            res.append(halftimes[1])
            return res,s
        if end_min<46:
            res.append(end)
            return res,s
        if end_min<90:
            res.append(halftimes[1])
            res.append(halftimes[2])
            res.append(end)
            return res,s
        else:
            res.append(halftimes[1])
            res.append(halftimes[2])
            res.append(halftimes[3])
            return res,s
    
    if start_min>45:
        s=1
        res.append(start)
        if end<90:
            res.append(end)
            return res,s
        else:
            res.append(halftimes[3])
            return res,s

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

def get_formation_wo_ball(team_df,ff,lf,invert):
    k=0
    formation=[]
    while k<len(team_df[ff:lf].mean(skipna = True))-2:
        if np.isnan(team_df.loc[ff][k]):
            k+=2
            continue
        formation.append([round(team_df[ff:lf].mean(skipna = True)[k],2)*invert,round(team_df[ff:lf].mean(skipna = True)[k+1],2)*invert])
        k+=2
    return formation


def get_avg_formations(team_df,frames,start,end,sapc,signs,do_check,possession):
    # Get the first and last frame of each halftime
    halftimes=get_halftime(team_df)
    # Adjust reduces the analysis time regarding start and end
    # Return s, to use the right sign
    analysis_time,s=cut_halftimes(halftimes,start,end)
    # Get substitutions during the analysis
    substitutions=get_substitutions(team_df,halftimes)
    #sapc in frames
    sapc = round(sapc*25)

    print('alles vorbereitet')
    formations=[]
    k=0
    print('analysis_time',analysis_time)
    print('frames',frames, 'sapc',sapc)
    while k < len(analysis_time):
        i = analysis_time[k]
        while i<analysis_time[k+1]:
            j=i+frames
            print('i,j',i,j)
            if j>analysis_time[k+1]:j=analysis_time[k+1]
            for substitution in substitutions:
                if substitution>i and substitution<j:
                    j=substitution
            print(i,j)
            if team_df[i:j].mean()['Ball']['BallPossession']>1 and team_df[i:j].mean()['Ball']['BallPossession']<2: #Test, ob es kein Ballbesitzwechsel gab
                print('Ball wechsel',i,j)
                i+=sapc+1 #3 Sekunden werden übersprungen
                print(i,j)
                continue
            if do_check:
                if team_df[i:j].mean()['Ball']['BallStatus']==0 or team_df[i:j].mean()['Ball']['BallPossession']!=possession: #Test, ob Ball nicht im Aus war oder #Test, ob richtige Mannschaft in Ballbesitz war
                    i=j+1
                    continue
            formations.append(get_formation_wo_ball(team_df,i,j,signs[s]))
            print('bin hier',i,j)
            i=j+1
            print(i,j)
        k+=2
        s+=1
    return formations

def get_avg_formations_STW(team_df,frames,signs,possession,start,end): #possesion 1/2
    # Get the first and last frame of each halftime
    halftimes=get_halftime(team_df)
    # Adjust reduces the analysis time regarding start and end
    # Return s, to use the right sign
    analysis_time,s=cut_halftimes(halftimes,start,end)
    # Get substitutions during the analysis
    substitutions=get_substitutions(team_df,halftimes)
    do_check,possession=check_possession(possession)
    formations=[]
    k=0
    while k < len(analysis_time):
        i = analysis_time[k]
        while i<analysis_time[k+1]:
            j=i+frames
            if j>analysis_time[k+1]:j=analysis_time[k+1]
            for substitution in substitutions:
                if substitution>i and substitution<j:
                    j=substitution

            if do_check:
                if team_df[i:j].mean()['Ball']['BallPossession']>1 and team_df[i:j].mean()['Ball']['BallPossession']<2: #Test, ob es kein Ballbesitzwechsel gab
                    i+=75+1 #3 Sekunden werden übersprungen
                    continue
                if team_df[i:j].mean()['Ball']['BallStatus']==1: #Test, ob Ball nicht im Aus war
                    if team_df[i:j].mean()['Ball']['BallPossession']==possession: #Test, ob richtige Mannschaft in Ballbesitz war
                        formations.append(get_formation_wo_ball(team_df,i,j,signs[s]))
            i+=25+1
        k+=2
        s+=1
    return formations