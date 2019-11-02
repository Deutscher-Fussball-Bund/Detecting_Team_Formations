from tacticon.RawEventDataReader import RawEventDataReader
from tacticon.Player import Player
import numpy as np

def get_avg_formations(path, first_frame, last_frame, team_id, game_section='firstHalf' or 'secondHalf'):
    """
    Berechnet die durchschnittliche Formation einer Mannschaft in einer gegebenen Zeitspanne.

    Argumente:
        path: Dateipfad zur XML-Datei die benutzt wird.
        first_frame: Beginn der Zeitspanne.
        last_frame: Ende der Zeitspanne.
        team_id: ID der Mannschaft die betrachtet werden soll.
        game_section: ...
    """
    # DE 'DFL-CLU-000N99'
    event_data = RawEventDataReader(path)
    player_columns=["X","Y","D","A","S","M","T","N"]

    player_positions=[]
    for frameset in event_data.xml_root.iter('FrameSet'):
        #if frameset.get('GameSection') != game_section:continue #Braucht man das noch?
        if frameset.get('TeamId') != team_id:continue
        #if frameset.get('PersonId') != 'DFL-OBJ-0000I4':continue
        print(frameset.get('PersonId'))

        player_df = event_data.create_player_dataframe(player_columns, frameset.get('PersonId'))
        ff, lf, abort = check_subs(player_df, first_frame, last_frame)
        if(abort):continue

        x_pos,y_pos=[],[]
        x_pos.append(Player(player_df, first_frame).meanFL('X', ff, lf))
        y_pos.append(Player(player_df, first_frame).meanFL('Y', ff, lf))
        player_positions.append([x_pos, y_pos])

    return player_positions

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
            print('Player was substituted in the time interval. Last frame: ' + LAST_FRAME)
            return first_frame, LAST_FRAME, False
    if(FIRST_FRAME > first_frame):
        if(LAST_FRAME < last_frame):
            print('Player was substituted in the time interval twice. First frame: ' + FIRST_FRAME + 'Last frame: ' + LAST_FRAME)
            return FIRST_FRAME, LAST_FRAME, False
        print('Player was substituted in the time interval. First frame: ' + FIRST_FRAME)
        return FIRST_FRAME, last_frame, False
    #Default
    return first_frame, last_frame, False