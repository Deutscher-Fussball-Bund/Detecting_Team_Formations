from tacticon.RawEventDataReader import RawEventDataReader
import pandas as pd
import numpy as np

def create_team_df(path, team_id):
    print('')
    print('Team Dataframe wird erstellt.')
    print('XML-Datei wird geladen.')
    event_data = RawEventDataReader(path)
    print('XML-Datei geladen.')

    team_df=pd.DataFrame()

    player_columns=["X","Y","N"]
    player_positions=[]
    person_ids=[]
    print('')
    print('Aktueller Fortschritt:')
    for frameset in event_data.xml_root.iter('FrameSet'):
        #Prüft ob der Spieler im richtigen Team ist und ob er schon betrachtet worden ist
        #Spieler können zweimal im Datensatz vorkommen, da es für erste und zweite Halbzeit FrameSets gibt
        if frameset.get('TeamId') != team_id:continue
        if (frameset.get('PersonId') in person_ids):continue

        print(frameset.get('PersonId'))
        person_ids.append(frameset.get('PersonId'))

        #Erstellt Player Dataframe
        player_df = event_data.create_player_dataframe(player_columns, frameset.get('PersonId'))
        
        #Erstellt aus dem Player Dataframe ein Pandas Dataframe und konkatiniert es mit dem Team Dataframe
        arrays=[[frameset.get('PersonId'),frameset.get('PersonId')],['X', 'Y']]
        tuples=list(zip(*arrays))
        index=pd.MultiIndex.from_tuples(tuples,names=['', ''])
        df=pd.DataFrame(player_df[['X','Y']].to_numpy(),index=player_df['N'].to_numpy(),columns=index)
        
        team_df=pd.concat([team_df, df],axis=1,sort=False)

    print('Team Dataframe erstellt.')
    return team_df

    """
    print(team_df.head())
    print('')
    print(team_df.tail())
    print('')
    print(team_df.loc[10003.0])
    print('')
    print(team_df.loc[173675.0])
    print('')
    print(team_df.loc[[10003.0]])
    print('')
    print(team_df.loc[[10003.0]]['DFL-OBJ-0027G6'])
    print('')
    print(team_df.loc[[10003.0]]['DFL-OBJ-0027G6'].values[0])
    print('')
    print(team_df.loc[[10003.0]]['DFL-OBJ-0027G6'].values[0][0])
    print(team_df.loc[[10003.0]]['DFL-OBJ-0027G6'].values[0][1])
    print('')
    val = team_df.loc[[10003.0]]['DFL-OBJ-0027G6']['X'].values[0]
    print('value is:', val)
    quit()
    """