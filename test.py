from minisom import MiniSom    
#from dashboard.scripts.test import get_formations
import pickle


import os
dirname=os.path.dirname(__file__)
path=os.path.join(dirname, '../uploads/')
matchinfo_dic= pickle.load( open( path+"matches.p", "rb" ) )
print(matchinfo_dic)
print(matchinfo_dic.keys())
for key in matchinfo_dic.keys():
    print(key)
print(list(matchinfo_dic)[1])
print(list(matchinfo_dic)[0][0])
quit()
del matchinfo_dic['Test_Id']
print(matchinfo_dic)
"""
matchinfo_dic['Test_Id']['Season']='Dummy Value'
matchinfo_dic['Test_Id']['PlannedKickoffTime']='Dummy Value'
matchinfo_dic['Test_Id']['HomeTeamName']='Dummy Value'
matchinfo_dic['Test_Id']['GuestTeamName']='Dummy Value'
matchinfo_dic['Test_Id']['Title']='Dummy Value'
matchinfo_dic['Test_Id']['Result']='Dummy Value'
matchinfo_dic['Test_Id']['StadiumName']='Dummy Value'
"""
#pickle.dump(matchinfo_dic, open( path+"matches.p", "wb" ) )


quit()



print(get_formations())
quit()

data = [[ 0.80,  0.55,  0.22,  0.03],
        [ 0.82,  0.50,  0.23,  0.03],
        [ 0.80,  -0.54,  0.22,  -0.03],
        [ -0.80,  0.53,  -0.26,  0.03],
        [ 0.79,  -0.56,  0.22,  -0.03],
        [ -0.75,  0.60,  -0.25,  0.03],
        [ 0.77,  0.59,  0.22,  0.03],
        [ 0.67,  0.69,  0.23,  0.04]] 

print('MiniSom wird erstellt.')
som = MiniSom(10, 10, 4, sigma=0.3, learning_rate=0.5) # initialization of 6x6 SOM
print('Erstellung abgeschlossen.')
print('Training beginnt.')
som.train_random(data, 100, True) # trains the SOM with 100 iterations
print('Training abgeschlossen.')
#print(som.get_weights())
print('')
print('win_map')
for cluster in som.win_map(data):
    print(cluster)
    print(som.win_map(data)[cluster])

print(som.quantization(data))
quit()

print('')
print('distance map')
print(som.distance_map())
import matplotlib.pyplot as plt
import numpy as np

plt.imshow(som.distance_map(), cmap='hot', interpolation='nearest')
plt.show()

print('')
print('activation_response')
print(som.activation_response(data))
import matplotlib.pyplot as plt
import numpy as np

plt.imshow(som.activation_response(data), cmap='hot', interpolation='nearest')
plt.show()

#print('')
#print('topographic_error')
#print(som.topographic_error(data))
#import matplotlib.pyplot as plt
#import numpy as np

#plt.imshow(som.topographic_error(data), cmap='hot', interpolation='nearest')
#plt.show()

#print('')
#print('labels_map')
#columns=['C1','C2','C3','C4','5','6','7','8']
#print(len(data),len(columns))
#print(som.labels_map(data,columns))
#import matplotlib.pyplot as plt
#import numpy as np

#plt.imshow(som.labels_map(data,columns), cmap='hot', interpolation='nearest')
#plt.show()