import os
import pickle
import xml.etree.ElementTree as ET

dic_path=os.path.join(os.path.dirname(__file__), '../../../uploads/matches.p')

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

def get_matchinformation():
    matchinfo_dic=pickle.load( open(dic_path, "rb" ) )
    information=[]
    for match_id in matchinfo_dic:
        match=[]
        match.append(matchinfo_dic[match_id]['Season'])
        match.append(matchinfo_dic[match_id]['PlannedKickoffTime'].split('T')[0])
        match.append(match_id)
        match.append(matchinfo_dic[match_id]['HomeTeamName'])
        match.append(matchinfo_dic[match_id]['GuestTeamName'])
        match.append(matchinfo_dic[match_id]['Result'])
        match.append(matchinfo_dic[match_id]['StadiumName'])
        information.append(match)
    return information

def get_matches():
    matchinfo_dic=pickle.load( open(dic_path, "rb" ) )
    information=[]
    for match_id in matchinfo_dic:
        match=[]
        match.append(matchinfo_dic[match_id]['Title'])
        match.append(match_id)
        information.append(match)
    return information

def get_teams(match_id):
    matchinfo_dic=pickle.load( open(dic_path, "rb" ) )
    information=[]
    information.append([matchinfo_dic[match_id]['HomeTeamName'],matchinfo_dic[match_id]['HomeTeamId']])
    information.append([matchinfo_dic[match_id]['GuestTeamName'],matchinfo_dic[match_id]['GuestTeamId']])
    return information

def extend_matchinfo_dic(path):
    matchinformation = ET.parse(path)
    root_matchinformation = matchinformation.getroot()

    matchinfo_dic=pickle.load(open(dic_path,'rb'))

    match_id=''
    for object in root_matchinformation.iter('General'):
        match_id=object.get('MatchId')
        matchinfo_dic[match_id]={}
        matchinfo_dic[match_id]['Season']=object.get('Season')
        matchinfo_dic[match_id]['PlannedKickoffTime']=object.get('PlannedKickoffTime').split('T')[0]
        matchinfo_dic[match_id]['HomeTeamName']=object.get('HomeTeamName')
        matchinfo_dic[match_id]['GuestTeamName']=object.get('GuestTeamName')
        matchinfo_dic[match_id]['Title']=object.get('HomeTeamName').replace('Nationalmannschaft','')+'- '+object.get('GuestTeamName').replace(' Nationalmannschaft','')
        matchinfo_dic[match_id]['Result']=object.get('Result')
    for object in root_matchinformation.iter('Environment'):
        matchinfo_dic[match_id]['StadiumName']=object.get('StadiumName')
    
    for object in root_matchinformation.iter('Team'):
        if object.get('TeamName')==matchinfo_dic[match_id]['HomeTeamName']:matchinfo_dic[match_id]['HomeTeamId']=object.get('TeamId')
        else: matchinfo_dic[match_id]['GuestTeamId']=object.get('TeamId')
    
    pickle.dump(matchinfo_dic,open(dic_path,'wb'))

def delete_row(row_id):
    matchinfo_dic=pickle.load(open(dic_path,'rb'))
    del matchinfo_dic[list(matchinfo_dic)[row_id]]
    pickle.dump(matchinfo_dic,open(dic_path,'wb'))

def indentify_team(match_id,team_id):
    bp,nbp=1,1
    matchinfo_dic=pickle.load( open(dic_path, "rb" ) )
    if team_id==matchinfo_dic[match_id]['HomeTeamId']:nbp=2
    else:bp=2

    return bp,nbp