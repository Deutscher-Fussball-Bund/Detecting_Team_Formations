import xml.etree.ElementTree as ET

def get_shitnumbers(person_ids, path):
    # XML wird geladen
    matchinformation = ET.parse(path)
    root_matchinformation = matchinformation.getroot()

    shirtnumbers=[]

    for id in person_ids:
        for player in root_matchinformation.iter('Player'):
            if(player.get('PersonId')==id):
                shirtnumbers.append(player.get('ShirtNumber'))
    
    return shirtnumbers