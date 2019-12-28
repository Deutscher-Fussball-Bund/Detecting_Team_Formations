from tacticon.RawEventDataReader import RawEventDataReader

from avg_formation import get_avg_formation, get_avg_formations
from hausdorff_metric import calculate_formation,calculate_formations
from array_operations import extract_formations

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

    event_data = RawEventDataReader(path)
    player_positions, shirtnumbers = get_avg_formations(event_data, time_intervall, 'DFL-CLU-000N99')
    print('')
    
    #player_positions = [[[-21.236895403064622, -4.544330446369087, -3.240826115922718], [-16.881978680879413, -13.246682211858761, 9.312365089940041]], [[-41.55300466355763, -23.541585609593604, -23.457041972018658], [-17.913850766155896, -24.683664223850766, -12.417528314457028]], [[-36.275636242504994, -23.014123917388407, -19.765922718187877], [2.5198134576948705, 13.908474350433046, 29.47172551632245]], [[-40.39473684210526, -26.074363757495, -33.77700866089274], [-10.95502331778814, -6.835469686875417, 10.300739506995338]], [[-25.151252498334443, -26.020706195869423, -32.11766822118588], [-27.857268487674883, -19.503764157228513, -4.046628914057296]], [[-39.15168554297135, -19.207288474350435, -22.97120586275816], [-21.073344437041975, -18.146568954030645, 7.922471685542972]], [[-23.432558294470354, -5.309960026648901, -10.552651565622917], [-12.453777481678882, -1.8568221185876082, 16.883924050632913]], [[-41.01299800133245, -25.982604930046634, -29.435822784810124], [-3.0687275149900066, 2.319493670886076, 24.174163890739507]], [[-36.21486342438374, -11.044243837441705, -5.633544303797469], [-27.255876082611593, -22.970759493670883, 5.7023317788141235]], [[-33.12347768154564, -15.901778814123917, -23.367441705529647], [-13.310086608927381, -5.98599600266489, 21.03724183877415]]]
    print('Positionsdaten sind geladen.')
    formations=extract_formations(player_positions)
    print('Formationen wurden extrahiert.')
    calculate_formations(formations)

    quit()


    #print('')
    #quit()
    player_positions, shirtnumbers = get_avg_formation(event_data, 30000, 50000, 'DFL-CLU-000N99')
    calculate_formation(player_positions)

    print('')