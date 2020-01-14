import os
import numpy as np
import pandas as pd

from start_analysis import start_analysis,start_clustering_matches,start_clustering_match
#from avg_formation import get_gks
#from team import create_team_df

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
#from tacticon.Pitch import Pitch
#from formations import get_formations

#from tacticon.RawEventDataReader import RawEventDataReader
#from matchinformation import get_gks
#from kmeans import calculate_cluster
from som import do_som
from kmeans2 import elbow,silhouette
"""
data=[[436, 162, 291, 248, 569, 590, 14, 659, 259, 361], [417, 85, 319, 36, 234, 472, 29, 660, 292, 199], [507, 381, 25, 454, 48, 15, 14, 337, 195, 434], [44,300, 84, 44, 512, 601, 278, 76, 94, 59], [653, 170, 331, 251, 21, 11, 10, 277, 173, 471], [55, 46, 334, 408, 49, 486, 18, 410, 23, 57], [362, 373, 118, 462, 78, 418, 178, 125, 417, 197], [386, 282, 214, 17, 474, 80, 541, 49, 32, 7], [211, 612, 67, 322, 63, 411, 378, 70, 772, 280], [438, 277, 186, 411, 1, 323, 426, 37, 726, 625]]
X=[]
i=0
for row in data:
    j=0
    for val in row:
        X.append([i,j,val])
        j+=1
    i+=1


from sklearn.cluster import KMeans
import numpy as np

#this is your array with the values
X = np.array(X)

#This function creates the classifier
#n_clusters is the number of clusters you want to use to classify your data
kmeans = KMeans(n_clusters=4, random_state=0).fit(X)

#you can see the labels with:
print(kmeans.labels_)

#or see were the centres of your clusters are
print(kmeans.cluster_centers_)

array=[]
k=0
for i in range(0,10):
    arr=[]
    for j in range(0,10):
        arr.append(kmeans.labels_[k])
        k+=1
    array.append(arr)

plt.imshow(array, cmap='Blues', interpolation='nearest')
plt.show()
quit()
"""
import pickle

#pickle.dump(formations, open( "formations_all.p", "wb" ) )
print('Lade Formation.')
formations = pickle.load( open( "formations_all.p", "rb" ) )
print('Formation geladen.')

#elbow(formations)
silhouette(formations)

quit()


"""
distance_map=[[0.00704436, 0.01232113, 0.01209842, 0.0120152, 0.01175659, 0.04415211, 0.16634495, 0.21088652, 0.25408186, 0.25819379, 0.31931615, 0.52049148, 0.29321199, 0.24061229, 0.28489977, 0.23548402, 0.30735389, 0.29407874, 0.32093328, 0.18105579], [0.0123154, 0.01972559, 0.02021515, 0.01956618, 0.01998965, 0.07814058, 0.31598147, 0.45762218, 0.38853098, 0.45708358, 0.52182329, 0.60344268, 0.45106066, 0.46037748, 0.34039512, 0.45170043, 0.46813566, 0.54041421, 0.59713447, 0.33276065], [0.01289006, 0.0205959, 0.01915814, 0.01880075, 0.02012335, 0.14003304, 0.37037628, 0.67750062, 0.68315481, 0.49523765, 0.59121903, 0.53867424, 0.65981618, 0.41351371, 0.43541006, 0.5414518, 0.48986616, 0.53479986, 0.5510697, 0.38925312], [0.01249911, 0.01971672, 0.0189131, 0.0216295, 0.10286149, 0.2047008, 0.5359718, 0.62574042, 0.81674135, 0.71345038, 0.63423196, 0.75928878, 0.5148549, 0.61826225, 0.50924856, 0.56403935, 0.49055053, 0.57471773, 0.66593265, 0.4364828], [0.01291206, 0.01861132, 0.02085931, 0.0580522, 0.24987313, 0.62158793, 0.5770214, 0.62297721, 0.60343076, 0.81212311, 0.8922635, 0.78812746, 0.77656008, 0.37818848, 0.43798878, 0.50250097, 0.61526996, 0.59003707, 0.6938931, 0.46884232], [0.0115152, 0.02150371, 0.01981493, 0.06058946, 0.36390057, 0.77412358, 0.77806339, 0.67196805, 0.66853598, 0.66896007, 0.63373925, 0.89678077, 0.85802717, 0.44521941, 0.39246743, 0.6632046, 0.55007696, 0.56441316, 0.65989515, 0.44494282], [0.01212848, 0.02025594, 0.02047634, 0.06564854, 0.30139986, 0.57033646, 0.66761013, 0.60841543, 0.60036075, 0.52469578, 0.47144184, 0.69658517, 0.93493561, 0.72174684, 0.57088963, 0.59879736, 0.62253919, 0.65471223, 0.75594579, 0.39852691], [0.01245505, 0.03201046, 0.03122014, 0.06673166, 0.27122356, 0.50477688, 0.48574522, 0.53393171, 0.5234124, 0.49043899, 0.42969291, 0.61446149, 0.81397098, 1.0, 0.69901674, 0.64526759, 0.75770724, 0.81370383, 0.85480656, 0.49797591], [0.16824259, 0.27956844, 0.29495356, 0.23508609, 0.36942214, 0.52856051, 0.43201992, 0.44254233, 0.50683636, 0.44865583, 0.45138083, 0.44090442, 0.65428836, 0.71962709, 0.62031833, 0.58967933, 0.52830144, 0.56206437, 0.82049883, 0.53304113], [0.35435179, 0.53803885, 0.56334339, 0.55642528, 0.38526163, 0.52728247, 0.51773768, 0.65898663, 0.51733046, 0.56426753, 0.47010736, 0.5544816, 0.63069752, 0.654463, 0.5984609, 0.41014406, 0.44659188, 0.44052387, 0.49815385, 0.40727347], [0.48222765, 0.71011708, 0.60725037, 0.56743775, 0.4782348, 0.6163337, 0.60497396, 0.49407493, 0.75355819, 0.50213117, 0.53461493, 0.65962929, 0.78991306, 0.58003661, 0.43932193, 0.60877228, 0.45552618, 0.50572698, 0.49380775, 0.35770114], [0.57282562, 0.99528977, 0.69126918, 0.57677791, 0.5288469, 0.70794411, 0.64895702, 0.6871935, 0.54243872, 0.44868817, 0.48777005, 0.84119435, 0.5335855, 0.52853683, 0.50982779, 0.56449831, 0.66402776, 0.4755314, 0.4674073, 0.30375981], [0.41792648, 0.6975605, 0.79109066, 0.61542492, 0.53223792, 0.69389958, 0.74596301, 0.78508243, 0.51682278, 0.46432407, 0.56745471, 0.55295279, 0.57944539, 0.44157215, 0.5963343, 0.60411184, 0.54888011, 0.57025505, 0.41417423, 0.24990105], [0.30947631, 0.61212488, 0.75579588, 0.65407362, 0.55038146, 0.56257282, 0.60395962, 0.59171862, 0.63873939, 0.50252977, 0.45853209, 0.58697944, 0.5602738, 0.48350282, 0.53384166, 0.67049595, 0.55635535, 0.54419894, 0.58554129, 0.23882722], [0.27699663, 0.52865783, 0.81816829, 0.75930164, 0.56737173, 0.55063903, 0.50660309, 0.55364147, 0.66028252, 0.53243371, 0.54772968, 0.56106152, 0.61654014, 0.56240272, 0.56293659, 0.42159916, 0.46930929, 0.32919301, 0.21924845, 0.13858722], [0.32319313, 0.62584259, 0.54552431, 0.75933546, 0.6632096, 0.55030876, 0.50925848, 0.43462303, 0.49639536, 0.5870367, 0.49595288, 0.46261609, 0.63134635, 0.60131793, 0.43395029, 0.53667812, 0.24910092, 0.09944752, 0.02623348, 0.01555107], [0.45958087, 0.51946999, 0.75886468, 0.60053739, 0.51241518, 0.4906016, 0.71176336, 0.48491614, 0.45121538, 0.30346449, 0.18961705, 0.20827598, 0.26912823, 0.35946863, 0.328826, 0.21310463, 0.11854136, 0.03033141, 0.02061862, 0.01330037], [0.38446562, 0.74767812, 0.69386328, 0.62960144, 0.53020863, 0.33834516, 0.42881662, 0.36782233, 0.18792698, 0.08110397, 0.02463926, 0.02292467, 0.05494858, 0.08713886, 0.08975442, 0.05688652, 0.02745065, 0.02047998, 0.02072024, 0.01298711], [0.54107107, 0.71395902, 0.70421851, 0.47616791, 0.31211524, 0.21242033, 0.10813197, 0.10384677, 0.05312386, 0.02029268, 0.02106417, 0.01877249, 0.01921934, 0.01888677, 0.0199882, 0.02061634, 0.02000183, 0.0218194, 0.02048602, 0.01273239], [0.28258936, 0.49546201, 0.34501019, 0.3388093, 0.25565324, 0.06623739, 0.01401692, 0.01191923, 0.01154638, 0.0123593, 0.01243792, 0.01190759, 0.01155447, 0.01200197, 0.01289121, 0.01227933, 0.01252986, 0.01333032, 0.01215956, 0.00747776]]
activation_response=[[0, 0, 0, 0, 0, 0, 0, 14, 7, 23, 18, 5, 65, 9,16, 66, 22, 52, 34, 47],[0, 0, 0, 0, 0, 0, 0, 23, 41, 15, 11, 13, 44, 33,170, 32, 27, 66, 8, 48],[0, 0, 0, 0, 0, 0, 0, 9, 9, 19, 8, 20, 14, 42,103, 22, 20, 38, 15, 12],[0, 0, 0, 0, 0, 0, 6, 8, 9, 13, 13, 8, 33, 4,38, 18, 23, 24, 18, 14],[0, 0, 0, 0, 0, 7, 0, 6, 0, 7, 9, 15, 22, 126,45, 67, 55, 23, 14, 6],[0, 0, 0, 0, 7, 22, 3, 8, 17, 15, 43, 18, 18, 63,58, 11, 26, 43, 12, 14],[0, 0, 0, 0, 0, 12, 25, 14, 11, 20, 38, 21, 13, 119,26, 26, 29, 40, 58, 16],[0, 0, 0, 0, 0, 32, 19, 12, 28, 20, 47, 19, 10, 10,0, 11, 46, 25, 4, 13],[0, 0, 4, 0, 0, 9, 17, 24, 26, 24, 18, 49, 46, 22,0, 19, 29, 32, 11, 12],[57, 157, 74, 49, 0, 4, 75, 8, 60, 13, 11, 8, 43, 6,16, 19, 24, 21, 65, 13],[12, 10, 12, 17, 0, 7, 10, 9, 6, 13, 10, 10, 5, 20,15, 12, 57, 15, 27, 10],[6, 17, 7, 4, 0, 8, 12, 6, 20, 26, 33, 16, 0, 11,27, 20, 5, 9, 11, 7],[22, 30, 10, 8, 23, 3, 13, 10, 18, 10, 9, 0, 27, 27,10, 10, 16, 11, 65, 21],[24, 9, 7, 15, 30, 0, 11, 24, 13, 21, 15, 0, 9, 27,10, 11, 4, 7, 17, 0],[17, 15, 11, 10, 21, 0, 28, 10, 9, 9, 5, 0, 15, 14,11, 17, 13, 0, 0, 0],[14, 13, 0, 8, 8, 0, 15, 12, 23, 82, 38, 0, 23, 12,17, 9, 0, 0, 0, 0],[12, 0, 5, 19, 7, 0, 5, 18, 7, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0],[10, 11, 7, 2, 8, 0, 3, 7, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0],[9, 8, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0],[15, 13, 15, 11, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0]]

print('')
print('distance_map')
print(distance_map)

plt.imshow(distance_map, cmap='Blues', interpolation='nearest')
plt.show()

print('')
print('activation_response')
print(activation_response)

plt.imshow(activation_response, cmap='Blues', interpolation='nearest')
plt.show()


from sklearn.cluster import KMeans
import numpy as np

#this is your array with the values
X = np.array(distance_map)

#This function creates the classifier
#n_clusters is the number of clusters you want to use to classify your data
kmeans = KMeans(n_clusters=6, random_state=0).fit(X)

#you can see the labels with:
print(kmeans.labels_)

#or see were the centres of your clusters are
print(kmeans.cluster_centers_)


quit()

"""









info_path_GER_EST=os.path.dirname(__file__) + '/../../../Daten/GER_EST/DFL_02_01_matchinformation_DFL-COM-000001_DFL-MAT-003BEU (1).xml'
path_GER_EST=os.path.dirname(__file__) + '/../../../Daten/GER_EST/DFL_04_03_positions_raw_observed_DFL-COM-000001_DFL-MAT-003BEU.xml'

info_path_GER_NL=os.path.dirname(__file__) + '/../../../Daten/GER_NL/DFL_02_01_matchinformation_DFL-COM-000001_DFL-MAT-X03BWS.xml' #'DFL-CLU-000N9A')#DFL-CLU-000N99
path_GER_NL=os.path.dirname(__file__) + '/../../../Daten/GER_NL/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml'

info_path_GER_BEL_U21=os.path.dirname(__file__) + '/../../../Daten/GER_BEL_U21/DFL_02_01_matchinformation_DFL-COM-000001_DFL-MAT-003BWT.xml'
path_GER_BEL_U21=os.path.dirname(__file__) + '/../../../Daten/GER_BEL_U21/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-003BWT.xml'

info_path_GER_NIR=os.path.dirname(__file__) + '/../../../Daten/GER_NIR/DFL_02_01_matchinformation_DFL-COM-000001_DFL-MAT-003BWS.xml'
path_GER_NIR=os.path.dirname(__file__) + '/../../../Daten/GER_NIR/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-003BWS.xml'



#info_path_GER_BEL_U21=os.path.dirname(__file__) + '/../../../Daten/GER_BEL_U21/DFL_02_01_matchinformation_DFL-COM-000001_DFL-MAT-003BWT.xml'
#path_GER_BEL_U21=os.path.dirname(__file__) + '/../../../Daten/GER_BEL_U21/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-003BWT.xml'


#formations=start_clustering_match(path_GER_BEL_U21,info_path_GER_BEL_U21)
#print(formations)
#print(len(formations))




matches=[[path_GER_EST,info_path_GER_EST],[path_GER_NL,info_path_GER_NL],[path_GER_NIR,info_path_GER_NIR],[path_GER_BEL_U21,info_path_GER_BEL_U21]]

cluster=start_clustering_matches(matches)
import pickle

pickle.dump(cluster, open( "formations_all.p", "wb" ) )
quit()
print('')
i=1
for formation in cluster:
    Pitch("#195905", "#faf0e6")
    for player in formation:
        plt.scatter(player[0], player[1], c='red', zorder=10)
        #plt.title(formation)
    plt.show()
    plt.savefig('Figure_'+str(i)+'.png')
    i+=1


formations=[[[-1.27, -4.56], [14.39, 22.18], [21.82, -13.35], [21.4, 10.16], [11.15, 4.8], [22.03, -3.36], [14.59, -6.36], [-0.5, 11.33], [12.05, 14.67], [5.36, -11.67]], [[-1.74, -2.03], [10.64, 25.32], [22.36, -11.77], [21.23, 13.73], [10.31, 8.3], [22.42, -1.13], [14.53, -3.02], [-1.5, 15.84], [11.49, 17.83], [5.43, -9.41]], [[-2.75, 0.08], [6.53, 26.96], [22.0, -10.64], [20.29, 15.97], [7.82, 10.65], [21.49, 0.57], [13.85, -0.11], [-3.66, 18.96], [10.09, 19.62], [4.57, -7.63]], [[-4.75, 1.6], [3.68, 27.06], [20.44, -10.12], [18.65, 16.18], [3.9, 11.51], [19.5, 1.15], [12.3, 1.79], [-6.23, 19.91], [7.95, 19.71], [2.68, -7.0]], [[-7.87, 2.64], [2.92, 26.51], [18.5, -10.35], [16.65, 14.88], [-0.16, 11.29], [17.42, 0.34], [10.14, 2.45], [-8.27, 19.03], [5.33, 18.47], [0.14, -7.6]], [[-11.36, 4.02], [3.28, 26.16], [16.91, -11.04], [14.43, 13.81], [-3.11, 11.15], [15.64, -0.83], [7.99, 2.54], [-9.8, 18.02], [2.84, 17.35], [-2.29, -8.5]], [[-14.41, 6.06], [2.91, 26.58], [15.61, -11.44], [12.52, 14.03], [-4.78, 11.8],[13.98, -1.24], [6.35, 3.03], [-11.56, 18.63], [0.79, 17.65], [-4.17, -8.52]], [[-16.67, 8.28], [1.06, 27.91], [14.07, -10.84], [11.52, 15.92], [-5.32, 13.34], [12.58, -0.05], [5.37, 4.25], [-13.53, 21.41], [-0.59, 19.74], [-5.42, -7.32]], [[-17.9, 9.66], [-0.78, 29.54], [12.81, -9.23], [11.85, 18.85], [-4.8, 15.13], [12.78, 2.82], [5.24, 5.83], [-14.53, 25.19], [-0.47, 22.92], [-6.03, -5.44]], [[-17.93, 10.11], [-0.79, 30.64], [12.84, -7.41], [13.27, 22.51], [-2.96, 16.86], [14.93, 7.01], [6.06, 7.24], [-13.64, 28.47], [1.58, 25.77], [-6.08, -3.55]], [[-16.81, 10.13], [1.53, 30.76], [14.2, -6.04], [15.32, 25.58], [-0.02, 18.35], [17.96, 11.67], [7.61, 8.24], [-11.25, 30.35], [5.22, 27.47], [-5.67, -1.99]], [[-15.21, 10.07], [4.72, 30.43], [16.02, -5.32], [17.78, 27.39], [3.07, 19.78], [19.91, 15.41], [9.33, 8.98], [-8.43, 31.1], [9.38, 27.51], [-4.96, -0.79]], [[-13.55, 9.96], [7.63, 30.29], [17.56, -4.92], [20.54,27.77], [5.96, 20.87], [20.5, 17.25], [10.9, 9.58], [-5.99, 31.41], [13.4, 26.65], [-4.05, 0.14]], [[-11.88, 9.73], [9.96, 30.78], [18.86, -4.66], [23.3, 27.53], [8.63, 21.28], [21.09, 17.13], [12.39, 10.06], [-4.03, 31.65], [16.59, 25.45], [-3.02, 0.88]], [[-10.25, 9.41], [11.81, 31.3], [20.03, -4.77], [25.59, 27.36], [11.31, 20.58], [22.83, 15.68], [13.89, 10.0], [-2.41, 31.74], [18.55, 24.32], [-1.89, 1.19]], [[-8.65, 9.0], [13.35, 31.43], [20.89, -5.36], [27.37, 26.91], [13.88, 19.05], [25.48, 13.49], [15.18, 9.09], [-0.96, 31.54], [19.11, 23.2], [-0.87, 0.91]]]
cluster=calculate_cluster(formations,2)
print(cluster)
for formation in cluster:
    Pitch("#195905", "#faf0e6")
    for player in formation:
        plt.scatter(player[0], player[1], c='red', zorder=10)
        #plt.title(formation)
    plt.show() 
quit()

start_analysis(os.path.dirname(__file__) + '/../Data_STS/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml',30,'DFL-CLU-000N99')

quit()

formations=get_formations()
for formation in formations:
    Pitch("#195905", "#faf0e6")
    for player in formations[formation]:
        plt.scatter(player[0], player[1], c='red', zorder=10)
        plt.title(formation)
    plt.show()  

quit()


team_df = create_team_df(os.path.dirname(__file__) + '/../Data_STS/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml', 'DFL-CLU-000N99')
#'/../Data_STS/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml', 'DFL-CLU-000N99')
#start_analysis(os.path.dirname(__file__) + '/../Data_STS/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml', 180, 'DFL-CLU-000N99')
#print('')
print('Torhüter werden entfernt.')
path=os.path.dirname(__file__) + '/../Data_STS/DFL_01_05_masterdata_DFL-CLU-000N99_DFL-SEA-0001K4_player.xml'
gk_ids = get_gks(path)
for gk in gk_ids:
    if gk in team_df.columns:
        team_df.drop(columns=[gk], level=0, inplace=True)

#print('')
#print('')
#print('')

#print(team_df.loc[122555.0])
#print(team_df.loc[122556.0])
#print(team_df.loc[122557.0])
#quit()

halftime=get_halftime(team_df)
substitutions=get_substitutions(team_df,halftime)
formations=make_intervalls(team_df,25000,halftime,substitutions)

for formation in formations:
    print('')
    Pitch("#195905", "#faf0e6")
    for player in formation:
        print(player)
        
        plt.scatter(player[0], player[1], c='red', zorder=10)
    plt.show()


quit()

# [[23,34],[344,45],..]

print('')
print('')

print(team_df[10003.0:10007.0])

print('')
print('')

print(team_df[10003.0:10007.0].mean())

print('')
for val in team_df[10003.0:10007.0].mean(skipna = True):
    print(val)
print('')

print('')
i=0
while i<len(team_df[10003.0:10007.0].mean(skipna = True)):
    print(team_df[10003.0:10007.0].mean(skipna = True)[i],team_df[10003.0:10007.0].mean(skipna = True)[i+1])
    i+=2
print('')
#isnull().values.any()

    

quit()
"""
arrays1 = [['Neuer', 'Neuer', 'Boateng', 'Boateng', 'Gnabry', 'Gnabry', 'Draxler', 'Draxler'],['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y']]
tuples1 = list(zip(*arrays1))
index1 = pd.MultiIndex.from_tuples(tuples1, names=['', ''])
df1 = pd.DataFrame(np.random.randn(3, 8), index=['10002', '10003', '10004'], columns=index1)
#print(df1)

arrays2 = [['Tah', 'Tah'],['X', 'Y']]
tuples2 = list(zip(*arrays2))
index2 = pd.MultiIndex.from_tuples(tuples2, names=['', ''])
df2 = pd.DataFrame(np.random.randn(2, 2), index=['10002', '10003'], columns=index2)
#print(df2)
df2 = pd.concat([df1, df2], axis=1, sort=False)
#print(df2)


arrays3 = [['Götze', 'Götze'],['X', 'Y']]
tuples3 = list(zip(*arrays3))
index3 = pd.MultiIndex.from_tuples(tuples3, names=['', ''])
df3 = pd.DataFrame(np.random.randn(1, 2), index=['10004'], columns=index3)
#print(df3)
df3 = pd.concat([df2, df3], axis=1, sort=False)
print(df3)


#print('')
#print(df3.loc[['10003']])
#print(df3.loc[['10003']]['Neuer'])
#print(df3.loc[['10003']]['Neuer']['X'])
#print('')
#print(df3['Tah'])
"""