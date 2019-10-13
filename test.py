import xml.etree.ElementTree as ET
import numpy as np
import os.path
import pickle 

# XML wird geladen
positionsRAW = ET.parse(os.path.dirname(__file__) + '/../Data_STS/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml')
matchInformation = ET.parse(os.path.dirname(__file__) + '/../Data_STS/DFL_02_01_matchinformation_DFL-COM-000001_DFL-MAT-X03BWS.xml')
root = positionsRAW.getroot()
rootMatchInfo = matchInformation.getroot()

#<FrameSet GameSection="firstHalf" MatchId="DFL-MAT-X03BWS" TeamId="DFL-CLU-000N9A" PersonId="DFL-OBJ-002G6R">
#<Object ObjectId="DFL-OBJ-002G6N" Type="player" Name="Frenkie de Jong" FirstName="Frenkie" LastName="de Jong" BirthDate="12.05.1997" CountryOfBirthGerman="Niederlande" CountryOfBirthEnglish="Netherlands" CountryOfBirthSpanish="Holanda" NationalityGerman="Niederländisch" NationalityEnglish="Dutch" NationalitySpanish="neerlandés" Height="180" Weight="74" ShirtNumber="21" PlayingPositionGerman="Mittelfeld" PlayingPositionEnglish="midField" PlayingPositionSpanish="medio campo" ClubId="DFL-CLU-000N9A" ClubName="Niederlande Nationalmannschaft"/>
#<Objects FeedType="player">
#<Object ObjectId="DFL-OBJ-0000O3" Type="player" Name="Marco Reus" FirstName="Marco" LastName="Reus" BirthDate="31.05.1989" BirthPlace="Dortmund" CountryOfBirthGerman="Deutschland" CountryOfBirthEnglish="Germany" CountryOfBirthSpanish="Alemania" NationalityGerman="Deutsch" NationalityEnglish="German" NationalitySpanish="alemán" Height="180" Weight="71" ShirtNumber="11" PlayingPositionGerman="Mittelfeld" PlayingPositionEnglish="midField" PlayingPositionSpanish="medio campo" ClubId="DFL-CLU-000N99" ClubName="Deutschland Nationalmannschaft"/>

playerPositionsFH = {}
playerPositionsSH = {}

for frameset in root.iter('FrameSet'):
    positionsX, positionsY = [], []
    for frame in frameset:
        positionsX.append(frame.get('X'))
        positionsY.append(frame.get('Y'))

    # String in Float umwandeln
    positionsX, positionsY = np.array(positionsX).astype(np.float), np.array(positionsY).astype(np.float)

    if (frameset.get('GameSection') == 'firstHalf'):
        playerPositionsFH[frameset.get('PersonId')] = {}
        playerPositionsFH[frameset.get('PersonId')]['Shortname'] = 'Ball'
        playerPositionsFH[frameset.get('PersonId')]['TeamId'] = frameset.get('TeamId')
        playerPositionsFH[frameset.get('PersonId')]['meanX'] = np.mean(positionsX)
        playerPositionsFH[frameset.get('PersonId')]['meanY'] = np.mean(positionsY)
    elif (frameset.get('GameSection') == 'secondHalf'):
        playerPositionsSH[frameset.get('PersonId')] = {}
        playerPositionsSH[frameset.get('PersonId')]['Shortname'] = 'Ball'
        playerPositionsSH[frameset.get('PersonId')]['TeamId'] = frameset.get('TeamId')
        playerPositionsSH[frameset.get('PersonId')]['meanX'] = np.mean(positionsX)
        playerPositionsSH[frameset.get('PersonId')]['meanY'] = np.mean(positionsY)
    else:
        print('Error: ', frameset.get('GameSection'))
    
for player in rootMatchInfo.iter('Player'):
    try: 
        playerPositionsFH[player.get('PersonId')]['Shortname'] = player.get('Shortname')
        playerPositionsSH[player.get('PersonId')]['Shortname'] = player.get('Shortname')
        playerPositionsFH[player.get('PersonId')]['ShirtNumber'] = player.get('ShirtNumber')
        playerPositionsSH[player.get('PersonId')]['ShirtNumber'] = player.get('ShirtNumber')
    except KeyError:
        print('KeyError: ' + player.get('Shortname') + ' hat nicht gespielt.')
    except:
        print('Error', player.get('PersonId'), player.get('Shortname'))

with open(os.path.dirname(__file__) + '/obj/playerPositionsFH.pkl', 'wb') as output:
    pickle.dump(playerPositionsFH, output, pickle.HIGHEST_PROTOCOL)
with open(os.path.dirname(__file__) + '/obj/playerPositionsSH.pkl', 'wb') as output:
    pickle.dump(playerPositionsSH, output, pickle.HIGHEST_PROTOCOL)