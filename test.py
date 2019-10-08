import xml.etree.ElementTree as ET
import numpy as np
import os.path

# XML wird geladen
tree = ET.parse(os.path.dirname(__file__) + '/../Data_STS/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml')
xmlPlayer = ET.parse(os.path.dirname(__file__) + '/../Data_STS/DFL_01_05_masterdata_DFL-CLU-000N99_DFL-SEA-0001K4_player.xml')
root = tree.getroot()
rootPlayer = xmlPlayer.getroot()


#<FrameSet GameSection="firstHalf" MatchId="DFL-MAT-X03BWS" TeamId="DFL-CLU-000N9A" PersonId="DFL-OBJ-002G6R">
#<Object ObjectId="DFL-OBJ-002G6N" Type="player" Name="Frenkie de Jong" FirstName="Frenkie" LastName="de Jong" BirthDate="12.05.1997" CountryOfBirthGerman="Niederlande" CountryOfBirthEnglish="Netherlands" CountryOfBirthSpanish="Holanda" NationalityGerman="Niederländisch" NationalityEnglish="Dutch" NationalitySpanish="neerlandés" Height="180" Weight="74" ShirtNumber="21" PlayingPositionGerman="Mittelfeld" PlayingPositionEnglish="midField" PlayingPositionSpanish="medio campo" ClubId="DFL-CLU-000N9A" ClubName="Niederlande Nationalmannschaft"/>
#<Objects FeedType="player">
#<Object ObjectId="DFL-OBJ-0000O3" Type="player" Name="Marco Reus" FirstName="Marco" LastName="Reus" BirthDate="31.05.1989" BirthPlace="Dortmund" CountryOfBirthGerman="Deutschland" CountryOfBirthEnglish="Germany" CountryOfBirthSpanish="Alemania" NationalityGerman="Deutsch" NationalityEnglish="German" NationalitySpanish="alemán" Height="180" Weight="71" ShirtNumber="11" PlayingPositionGerman="Mittelfeld" PlayingPositionEnglish="midField" PlayingPositionSpanish="medio campo" ClubId="DFL-CLU-000N99" ClubName="Deutschland Nationalmannschaft"/>
players = []
playerPositions = {}
for player in rootPlayer.iter('Object'):
    playerPositions[player.get('Name')]['ObjectId'] = player.get('ObjectId')
    #players.append([player.get('ObjectId'), player.get('Name')])
print(playerPositions)

playerPositions2 = []
for frameset in root.iter('FrameSet'):
    positions = []
    for frame in frameset:
        positions.append(frame.get('X'))
        # print(frame.get('X'))

    # String in Float umwandeln
    positions = np.array(positions).astype(np.float)
    # frameset.get('TeamId')
    playerPositions2.append([frameset.get('PersonId'), frameset.get('GameSection'), np.mean(positions)])

new_dic = {}
new_dic[1] = {}
new_dic[1][2] = 5
for player in players:
    for position in playerPositions2:
        if player[0] in position:

            print(player[1] + ':', position[2], position[1])