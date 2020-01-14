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

def get_gks(path):
    # XML wird geladen
    matchinformation = ET.parse(path)
    root_matchinformation = matchinformation.getroot()

    gk_ids=[]
    for object in root_matchinformation.iter('Player'):
            if(object.get('PlayingPosition')=='TW'):
                gk_ids.append(object.get('PersonId'))

    print('Torhüter', gk_ids)
    return gk_ids

def get_team_ids(path):
    matchinformation = ET.parse(path)
    root_matchinformation = matchinformation.getroot()

    team_ids=[]
    for object in root_matchinformation.iter('Team'):
        team_ids.append(object.get('TeamId'))

    print('Teams', team_ids)
    return team_ids

def get_match_id(info_string):
    root_matchinformation = ET.fromstring(info_string)
    #root_matchinformation = matchinformation.getroot()

    for object in root_matchinformation.iter('General'):
        return object.get('MatchId')

def get_match_id_from_position(path):
    matchinformation = ET.parse(path)
    root_matchinformation = matchinformation.getroot()

    for object in root_matchinformation.iter('MetaData'):
        return object.get('MatchId')

def get_match_title(info_string):
    root_matchinformation = ET.fromstring(info_string)
    #root_matchinformation = matchinformation.getroot()

    for object in root_matchinformation.iter('General'):
        return object.get('MatchTitle')

def get_matchinformation(path):
    matchinformation = ET.parse(path)
    root_matchinformation = matchinformation.getroot()
    information=[]
    for object in root_matchinformation.iter('General'):
        information.append(object.get('Season'))
        information.append(object.get('PlannedKickoffTime').split('T')[0])
        information.append(object.get('MatchId'))
        information.append(object.get('HomeTeamName'))
        information.append(object.get('GuestTeamName'))
        information.append(object.get('Result'))
    for object in root_matchinformation.iter('Environment'):
        information.append(object.get('StadiumName'))
    return information