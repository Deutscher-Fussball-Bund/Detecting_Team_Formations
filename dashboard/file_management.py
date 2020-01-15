import os
import shutil
import base64
import numpy as np
import pandas as pd

from dashboard.scripts.matchinformation import get_match_id,get_match_title,get_match_id_from_position,get_matchinformation,get_matches,get_teams,extend_matchinfo_dic,delete_row


def new_match(fileName, contents):
    content_type, content_string = contents.split(',')
    decoded_matchinfo = base64.b64decode(content_string).decode('utf-8')

    dirname=os.path.dirname(__file__)
    path=os.path.join(dirname, '../../uploads/')
    #filename=path+fileName
    match_id=get_match_id(decoded_matchinfo)
    match_title=get_match_title(decoded_matchinfo)

    path=create_match_folder(path,match_id)
    if path==None:
        print('Spiel wurde schon hochgeladen.')
        return
    filename=path+'/matchinformation_'+match_id+'.xml'
    with open(filename, "w") as f:
        f.write(decoded_matchinfo)
    print('Datei verschoben.')
    extend_matchinfo_dic(filename)
    return match_title

def create_match_folder(path,match_id):
    # define the name of the directory to be created
    path+=match_id

    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
        return None
    else:
        print ("Successfully created the directory %s " % path)
        return path

def move_match(fileNames):
    fileName=fileNames[-1]
    dirname=os.path.dirname(__file__)
    path=os.path.join(dirname, '../../uploads/')
    filename=path+fileName
    match_id=get_match_id_from_position(filename)
    shutil.move(filename,path+match_id+'/positions_raw_'+match_id+'.xml')

def create_match_table():
    columns = ['Season','Date', 'MatchId', 'HomeTeam', 'GuestTeam', 'Result', 'Stadium']
    data=np.array(get_matchinformation())
    df=pd.DataFrame(data,columns=columns)
    return df

def get_match_list():
    return get_matches()

def get_team_list(match_id):
    return get_teams(match_id)

def delete_selected_rows(selected_rows):
    for row_id in selected_rows:
        delete_row(row_id)
