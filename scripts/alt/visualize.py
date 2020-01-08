from tacticon.Pitch import Pitch
import pickle
import os
import matplotlib.pyplot as plt

players = []

with open(os.path.dirname(__file__) + '/obj/playerPositionsFH.pkl', 'rb') as input:
    playerPositionsFH = pickle.load(input)
with open(os.path.dirname(__file__) + '/obj/playerPositionsSH.pkl', 'rb') as input:
    playerPositionsSH = pickle.load(input)

# Intersection to find out which player played in both halftimes
fhSet = set(playerPositionsFH)
shSet = set(playerPositionsSH)
for playerId in fhSet.intersection(shSet):
    if (playerPositionsFH[playerId].get('TeamId') != 'DFL-CLU-000N99'):
        continue
    name = playerPositionsFH[playerId].get('Shortname')
    x1 = playerPositionsFH[playerId].get('meanX')
    x2 = playerPositionsSH[playerId].get('meanX') * -1
    y1 = playerPositionsFH[playerId].get('meanY')
    y2 = playerPositionsSH[playerId].get('meanY') * -1
    players.append([name, (x1, y1), (x2,y2)])


Pitch("#195905", "#faf0e6")
for player in players:
    plt.annotate(player[0], xy=player[1], xytext=player[2],
                    arrowprops=dict(arrowstyle="->"), zorder=10)
plt.show()