from dashboard.scripts.hausdorff_metric import calculate_formation,calculate_formations
from dashboard.scripts.avg_formation import get_avg_formations,get_avg_formations_STW
from dashboard.scripts.kmeans import calculate_cluster
from dashboard.scripts.array_operations import move_formations_to_centre_spot
from dashboard.scripts.matchinformation import indentify_team

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


def start_clustering_matches(tdfs,match_id_team_id_pair,sapc,n_cluster,possession):
    print('')
    print(len(tdfs),len(match_id_team_id_pair))
    formations=[]
    for [team_df,signs],[match_id,team_id] in zip(tdfs,match_id_team_id_pair):
        do_check,possession = check_possession(possession,match_id,team_id)
        # Sliding Time Window ist immer 3 Sekunden groß
        frames=3*25
        print('Get Formations',match_id,team_id)
        formations+=get_avg_formations_STW(team_df,frames,sapc,signs,do_check,possession)

    print('Formationen normalisieren.')
    formations=move_formations_to_centre_spot(formations)

    print('Calculate Cluster')
    clusters=calculate_cluster(formations,n_cluster)
    return clusters


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