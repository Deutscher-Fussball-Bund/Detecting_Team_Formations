import os
from tacticon.RawEventDataReader import RawEventDataReader

from hausdorff_metric import calculate_formation,calculate_formations
from team import create_team_df,exclude_gks,add_ball_details
from avg_formation import get_avg_formations,get_avg_formations_by_timeframes

def start_analysis(path, time_intervall, team_id):
    """
    Startet die Analyse.

    Argumente:
        path: Dateipfad zur XML-Datei die benutzt wird.
        time_intervall: Die Länge des Zeitintervall, das je Detektion benutzt wird. Angabe in Sekunden.
        team_id: ID der Mannschaft die betrachtet werden soll.
    """
    print('')
    print('Positionsdaten werden geladen.')
    print('XML-Datei wird geladen.')
    event_data = RawEventDataReader(path)
    print('XML-Datei geladen.')
    team_df=create_team_df(event_data,'DFL-CLU-000N99')
    print('Torhüter werden entfernt.')
    path=os.path.dirname(__file__) + '/../Data_STS/DFL_01_05_masterdata_DFL-CLU-000N99_DFL-SEA-0001K4_player.xml'
    team_df=exclude_gks(team_df,path)
    frames=time_intervall*25
    formations=get_avg_formations(team_df,frames)
    calculate_formations(formations)

def start_clustering(path, team_id):
    print('')
    print('Positionsdaten werden geladen.')
    print('XML-Datei wird geladen.')
    event_data = RawEventDataReader(path)
    print('XML-Datei geladen.')
    team_df=create_team_df(event_data,team_id)
    team_df=add_ball_details(event_data,team_df)
    formations=get_avg_formations_by_timeframes(team_df,75)
    print(formations)
    #calculate_formations(formations)