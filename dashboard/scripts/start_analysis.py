import os
from dashboard.scripts.tacticon.RawEventDataReader import RawEventDataReader

from dashboard.scripts.hausdorff_metric import calculate_formation,calculate_formations
from dashboard.scripts.avg_formation import get_avg_formations
from dashboard.scripts.kmeans import calculate_cluster
from dashboard.scripts.array_operations import move_formations_to_centre_spot
from dashboard.scripts.matchinformation import get_team_ids,indentify_team

def start_analysis(team_df,signs,match_id,team_id,time_intervall,possession,start,end,sapc):
    """
    Startet die Analyse.

    Argumente:
        path: Dateipfad zur XML-Datei die benutzt wird.
        info_path: Dateipfad zur Matchinfo-xml
        time_intervall: Die Länge des Zeitintervall, das je Detektion benutzt wird. Angabe in Sekunden.
        team_id: ID der Mannschaft die betrachtet werden soll.
        possession: Ballbesitz
        start: Anfang der Analyse (Spielminute)
        end: Ende der Analyse (Spielminute)
        sapc: seconds after possession change
    """
    do_check,possession = check_possession(possession,match_id,team_id)
    frames=time_intervall*25
    print('Get Formations')
    formations=get_avg_formations(team_df,frames,start,end,sapc,signs,do_check,possession)

    if not formations:
        return False,0,0,0,0

    print('Calculate Formations')
    avg_formation,hd_min=calculate_formation(formations)
    print('++++++++++++++++++')
    hd_mins=calculate_formations(formations)
    return True,avg_formation,hd_min,formations,hd_mins

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
    #formations_old=get_avg_formations_by_timeframes_old(team_df,75,signs)
    print('Old fertig.')
    #formations_new=get_avg_formations_by_timeframes(team_df,75,signs)
    print('New fertig.')
    print('Formationen normalisieren.')
    #formations_old=move_formations_to_centre_spot(formations_old)
    #formations_new=move_formations_to_centre_spot(formations_new)
    print('')
      
    #cluster_old=calculate_cluster(formations_old,10)
    #cluster_new=calculate_cluster(formations_new,10)
    #return [cluster_old,cluster_new]

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
        #formations+=get_avg_formations_by_timeframes(team_df,75,signs)
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
            #formations+=get_avg_formations_by_timeframes2(team_df,75,signs,1)
            print('Länge',len(formations))

    print('Formationen normalisieren.')
    #formations=move_formations_to_centre_spot(formations)
    print('')
    
    cluster=calculate_cluster(formations,20)
    return cluster



def check_possession(possession,match_id,team_id):
    """
    Prüft, ob die Mannschaft Heim oder Auswärtsteam ist und gibt zurück, ob der Ballbesitz geprüft werden soll
    """
    bp,npb=indentify_team(match_id,team_id)
    if possession=='bp':
        return True,bp
    if possession=='nbp':
        return True,npb
    if possession=='bo':
        return False,0