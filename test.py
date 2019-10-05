import xml.etree.ElementTree as ET
import numpy as np

#XML wird geladen
#tree = ET.parse('DATA_STS/position_half.xml')
tree = ET.parse('Data_STS/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml')
root = tree.getroot()
#print(root)


#<FrameSet GameSection="firstHalf" MatchId="DFL-MAT-X03BWS" TeamId="DFL-CLU-000N9A" PersonId="DFL-OBJ-002G6R">
#<Object ObjectId="DFL-OBJ-002G6N" Type="player" Name="Frenkie de Jong" FirstName="Frenkie" LastName="de Jong" BirthDate="12.05.1997" CountryOfBirthGerman="Niederlande" CountryOfBirthEnglish="Netherlands" CountryOfBirthSpanish="Holanda" NationalityGerman="Niederländisch" NationalityEnglish="Dutch" NationalitySpanish="neerlandés" Height="180" Weight="74" ShirtNumber="21" PlayingPositionGerman="Mittelfeld" PlayingPositionEnglish="midField" PlayingPositionSpanish="medio campo" ClubId="DFL-CLU-000N9A" ClubName="Niederlande Nationalmannschaft"/>
        
for frameset in root.iter('FrameSet'):
    positions = []
    for frame in frameset:
        positions.append(frame.get('X'))
        #print(frame.get('X'))

    #String in Float umwandeln
    positions = np.array(positions).astype(np.float)

    print(frameset.get('TeamId'), frameset.get('GameSection'), frameset.get('PersonId'), np.mean(positions))