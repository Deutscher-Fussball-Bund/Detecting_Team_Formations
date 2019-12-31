import os
from tacticon.RawEventDataReader import RawEventDataReader

from hausdorff_metric import calculate_formation,calculate_formations
from team import create_team_df,exclude_gks
from avg_formation import get_avg_formations

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

    team_df=create_team_df(path,'DFL-CLU-000N99')
    print('Torhüter werden entfernt.')
    path=os.path.dirname(__file__) + '/../Data_STS/DFL_01_05_masterdata_DFL-CLU-000N99_DFL-SEA-0001K4_player.xml'
    team_df=exclude_gks(team_df,path)
    frames=time_intervall*25
    formations=get_avg_formations(team_df,frames)
    calculate_formations(formations)

    quit()
