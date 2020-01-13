import os
from dashboard.scripts.tacticon.RawEventDataReader import RawEventDataReader

from dashboard.scripts.hausdorff_metric import calculate_formation,calculate_formations
from dashboard.scripts.team import create_team_df,exclude_gks,add_ball_details
from dashboard.scripts.avg_formation import get_avg_formations,get_avg_formations_by_timeframes
from dashboard.scripts.kmeans import calculate_cluster
from dashboard.scripts.array_operations import move_formations_to_centre_spot
from dashboard.scripts.matchinformation import get_team_ids

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

def start_clustering_team(path,info_path,team_id):
    print('')
    print('Positionsdaten werden geladen.')
    print('XML-Datei wird geladen.')
    event_data = RawEventDataReader(path)
    print('XML-Datei geladen.')
    team_df=create_team_df(event_data,team_id)
    print('Torhüter werden entfernt.')
    team_df,signs=exclude_gks(team_df,info_path)
    print('Ballinformationen werden hinzugefügt.')
    team_df=add_ball_details(event_data,team_df)
    print('Sliding Time Windows werden erstellt.')
    formations=get_avg_formations_by_timeframes(team_df,75,signs)
    print('Formationen normalisieren.')
    formations=move_formations_to_centre_spot(formations)
    print('')
    
    cluster=calculate_cluster(formations,4)
    return cluster

def start_clustering_match(path,info_path):
    print('')
    print('Positionsdaten werden geladen.')
    print('XML-Datei wird geladen.')
    event_data = RawEventDataReader(path)
    print('XML-Datei geladen.')
    formations=[]
    team_ids=get_team_ids(info_path)
    for team_id in team_ids:
        team_df=create_team_df(event_data,team_id)
        print('Torhüter werden entfernt.')
        team_df,signs=exclude_gks(team_df,info_path)
        print('Ballinformationen werden hinzugefügt.')
        team_df=add_ball_details(event_data,team_df)
        print('Sliding Time Windows werden erstellt.')
        formations+=get_avg_formations_by_timeframes(team_df,75,signs)
        print('Länge',len(formations))
    print('Formationen normalisieren.')
    formations=move_formations_to_centre_spot(formations)
    print('')
    
    cluster=calculate_cluster(formations,4)
    return cluster

def start_clustering_matches(matches):
    print('')
    formations=[]
    for match in matches:
        path=match[0]
        info_path=match[1]
        print('Positionsdaten werden geladen.')
        print('XML-Datei wird geladen.')
        event_data = RawEventDataReader(path)
        print('XML-Datei geladen.')
        
        team_ids=get_team_ids(info_path)
        for team_id in team_ids:
            team_df=create_team_df(event_data,team_id)
            print('Torhüter werden entfernt.')
            team_df,signs=exclude_gks(team_df,info_path)
            print('Ballinformationen werden hinzugefügt.')
            team_df=add_ball_details(event_data,team_df)
            print('Sliding Time Windows werden erstellt.')
            formations+=get_avg_formations_by_timeframes(team_df,75,signs)
            print('Länge',len(formations))

    print('Formationen normalisieren.')
    formations=move_formations_to_centre_spot(formations)
    print('')
    
    cluster=calculate_cluster(formations,20)
    return cluster