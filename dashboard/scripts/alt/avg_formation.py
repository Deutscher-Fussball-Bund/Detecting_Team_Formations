import os.path
import numpy as np

from tacticon.RawEventDataReader import RawEventDataReader
from tacticon.Player import Player
from matchinformation import get_shitnumbers, get_gks

def get_avg_formations(event_data, time_intervall, team_id):
    """
    Berechnet die durchschnittliche Formation einer Mannschaft in einer gegebenen Zeitspanne.

    Argumente:
        path: Dateipfad zur XML-Datei die benutzt wird.
        first_frame: Beginn der Zeitspanne.
        last_frame: Ende der Zeitspanne.
        team_id: ID der Mannschaft die betrachtet werden soll.
    """

    player_columns=["X","Y","D","A","S","M","T","N"]
    #Unbedingt bessere Lösung!!
    path=os.path.dirname(__file__) + '/../Data_STS/DFL_01_05_masterdata_DFL-CLU-000N99_DFL-SEA-0001K4_player.xml'
    gk_ids = get_gks(path)

    player_positions=[]
    person_ids=[]
    #Da eine Sekunde aus 25 Frames besteht
    time_intervall *= 25
    print('Aktueller Fortschritt:')
    for frameset in event_data.xml_root.iter('FrameSet'):
        #Prüft ob der Spieler im richtigen Team ist und ob er schon betrachtet worden ist
        #Spieler können zweimal im Datensatz vorkommen, da es für erste und zweite Halbzeit FrameSets gibt
        if frameset.get('TeamId') != team_id:continue
        if (frameset.get('PersonId') in gk_ids):continue
        if (frameset.get('PersonId') in person_ids):continue

        print(frameset.get('PersonId'))
        person_ids.append(frameset.get('PersonId'))

        #Erstellt Player DataFrame und prüft, ob er Spieler im gegebenen Zeitintervall auf dem Feld stand
        player_df = event_data.create_player_dataframe(player_columns, frameset.get('PersonId'))
        first_frame,last_frame = get_time_frames(player_df)
        ff, lf, abort = check_subs(player_df, first_frame, last_frame)
        if(abort):continue

        x_pos,y_pos=[],[]
        
        ff=int(ff)
        lf=int(lf)
        for i in range(ff, lf+1, time_intervall):
            print('hier: i, ff, lf, time_intervall', i,ff,lf,time_intervall)       
            #Durchschnittliche X- und Y-Position für Spieler wird berechnet
            x_pos.append(Player(player_df, ff).meanFL('X', i,i + time_intervall))
            y_pos.append(Player(player_df, ff).meanFL('Y', i,i + time_intervall))

        player_positions.append([x_pos, y_pos])

    #Muss noch dynamisch gesetzt werden
    path=os.path.dirname(__file__) + '/../Data_STS/DFL_02_01_matchinformation_DFL-COM-000001_DFL-MAT-X03BWS.xml'
    shirtnumbers=get_shitnumbers(person_ids,path)
    print('Alle Spieler wurden geladen.')
    return player_positions, shirtnumbers



def get_avg_formation(event_data, team_id):
    """
    Berechnet die durchschnittliche Formation einer Mannschaft in einer gegebenen Zeitspanne.

    Argumente:
        path: Dateipfad zur XML-Datei die benutzt wird.
        first_frame: Beginn der Zeitspanne.
        last_frame: Ende der Zeitspanne.
        team_id: ID der Mannschaft die betrachtet werden soll.
    """

    #Unbedingt bessere Lösung!!
    path=os.path.dirname(__file__) + '/../Data_STS/DFL_01_05_masterdata_DFL-CLU-000N99_DFL-SEA-0001K4_player.xml'
    gk_ids = get_gks(path)

    player_positions=[]
    person_ids=[]
    print('Aktueller Fortschritt:')
    for frameset in event_data.xml_root.iter('FrameSet'):
        #Prüft ob der Spieler im richtigen Team ist und ob er schon betrachtet worden ist
        #Spieler können zweimal im Datensatz vorkommen, da es für erste und zweite Halbzeit FrameSets gibt
        if frameset.get('TeamId') != team_id:continue
        if (frameset.get('PersonId') in gk_ids):continue
        if (frameset.get('PersonId') in person_ids):continue

        print(frameset.get('PersonId'))
        person_ids.append(frameset.get('PersonId'))

        #Erstellt Player DataFrame und prüft, ob er Spieler im gegebenen Zeitintervall auf dem Feld stand
        player_df = event_data.create_player_dataframe(player_columns, frameset.get('PersonId'))
        first_frame,last_frame = get_time_frames(player_df)
        ff, lf, abort = check_subs(player_df, first_frame, last_frame)
        if(abort):continue

        #Durchschnittliche X- und Y-Position für Spieler wird berechnet
        #x_pos,y_pos=[],[]
        x_pos=Player(player_df, ff).meanFL('X', ff, lf)
        y_pos=Player(player_df, ff).meanFL('Y', ff, lf)

        player_positions.append([x_pos, y_pos])

    #Muss noch dynamisch gesetzt werden
    path=os.path.dirname(__file__) + '/../Data_STS/DFL_02_01_matchinformation_DFL-COM-000001_DFL-MAT-X03BWS.xml'
    shirtnumbers=get_shitnumbers(person_ids,path)
    print('Alle Spieler wurden geladen.')
    return player_positions, shirtnumbers

def get_time_frames(player_df):
    first_frame = player_df['N'][0]
    last_frame = player_df['N'].iloc[-1]
    return first_frame, last_frame

def check_subs(player_df, first_frame, last_frame):
    """
    Prüft, ob der Spieler in dem angegebenen Zeitintervall auf dem Feld war.

    Argumente:
        player_df: Datenframe des Spielers.
        first_frame: Beginn der Zeitspanne.
        last_frame: Ende der Zeitspanne.
    """
    FIRST_FRAME = player_df['N'][0]
    LAST_FRAME = player_df['N'].iloc[-1]

    if(LAST_FRAME < first_frame):
        print('Player was substituted before the time interval.')
        return first_frame, last_frame, True
    if(FIRST_FRAME > last_frame):
        print('Player was substituted after the time interval.')
        return first_frame, last_frame, True
    if(FIRST_FRAME < first_frame):
        if(LAST_FRAME < last_frame):
            print('Player was substituted in the time interval. Last frame: ' + str(LAST_FRAME))
            return first_frame, LAST_FRAME, False
    if(FIRST_FRAME > first_frame):
        if(LAST_FRAME < last_frame):
            print('Player was substituted in the time interval twice. First frame: ' + str(FIRST_FRAME) + 'Last frame: ' + str(LAST_FRAME))
            return FIRST_FRAME, LAST_FRAME, False
        print('Player was substituted in the time interval. First frame: ' + str(FIRST_FRAME))
        return FIRST_FRAME, last_frame, False
    #Default
    return first_frame, last_frame, False