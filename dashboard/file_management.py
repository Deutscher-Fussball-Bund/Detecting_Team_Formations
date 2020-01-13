import os
import shutil
import base64
import numpy as np
import pandas as pd

from dashboard.scripts.matchinformation import get_match_id,get_match_title,get_match_id_from_position,get_matchinformation


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
    matchinformation=[]

    dirname=os.path.dirname(__file__)
    path=os.path.join(dirname, '../../uploads/')
    for dir in os.listdir(path):
        if dir=='.DS_Store':continue
        for file in os.listdir(path+dir):
            if 'matchinformation' in file:
                matchinformation.append(get_matchinformation(path+dir+'/'+file))
    data=np.array(matchinformation)
    df=pd.DataFrame(data,columns=columns)
    return df
