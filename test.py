from minisom import MiniSom    
#from dashboard.scripts.test import get_formations
import pickle


import os
import pandas as pd
import numpy as np

print("F2".split("F")[1])
quit()


formations=[[[-1.27, -4.56], [14.39, 22.18], [21.82, -13.35], [21.4, 10.16], [11.15, 4.8], [22.03, -3.36], [14.59, -6.36], [-0.5, 11.33], [12.05, 14.67], [5.36, -11.67]], [[-1.74, -2.03], [10.64, 25.32], [22.36, -11.77], [21.23, 13.73], [10.31, 8.3], [22.42, -1.13], [14.53, -3.02], [-1.5, 15.84], [11.49, 17.83], [5.43, -9.41]], [[-2.75, 0.08], [6.53, 26.96], [22.0, -10.64], [20.29, 15.97], [7.82, 10.65], [21.49, 0.57], [13.85, -0.11], [-3.66, 18.96], [10.09, 19.62], [4.57, -7.63]], [[-4.75, 1.6], [3.68, 27.06], [20.44, -10.12], [18.65, 16.18], [3.9, 11.51], [19.5, 1.15], [12.3, 1.79], [-6.23, 19.91], [7.95, 19.71], [2.68, -7.0]], [[-7.87, 2.64], [2.92, 26.51], [18.5, -10.35], [16.65, 14.88], [-0.16, 11.29], [17.42, 0.34], [10.14, 2.45], [-8.27, 19.03], [5.33, 18.47], [0.14, -7.6]], [[-11.36, 4.02], [3.28, 26.16], [16.91, -11.04], [14.43, 13.81], [-3.11, 11.15], [15.64, -0.83], [7.99, 2.54], [-9.8, 18.02], [2.84, 17.35], [-2.29, -8.5]], [[-14.41, 6.06], [2.91, 26.58], [15.61, -11.44], [12.52, 14.03], [-4.78, 11.8],[13.98, -1.24], [6.35, 3.03], [-11.56, 18.63], [0.79, 17.65], [-4.17, -8.52]], [[-16.67, 8.28], [1.06, 27.91], [14.07, -10.84], [11.52, 15.92], [-5.32, 13.34], [12.58, -0.05], [5.37, 4.25], [-13.53, 21.41], [-0.59, 19.74], [-5.42, -7.32]], [[-17.9, 9.66], [-0.78, 29.54], [12.81, -9.23], [11.85, 18.85], [-4.8, 15.13], [12.78, 2.82], [5.24, 5.83], [-14.53, 25.19], [-0.47, 22.92], [-6.03, -5.44]], [[-17.93, 10.11], [-0.79, 30.64], [12.84, -7.41], [13.27, 22.51], [-2.96, 16.86], [14.93, 7.01], [6.06, 7.24], [-13.64, 28.47], [1.58, 25.77], [-6.08, -3.55]], [[-16.81, 10.13], [1.53, 30.76], [14.2, -6.04], [15.32, 25.58], [-0.02, 18.35], [17.96, 11.67], [7.61, 8.24], [-11.25, 30.35], [5.22, 27.47], [-5.67, -1.99]], [[-15.21, 10.07], [4.72, 30.43], [16.02, -5.32], [17.78, 27.39], [3.07, 19.78], [19.91, 15.41], [9.33, 8.98], [-8.43, 31.1], [9.38, 27.51], [-4.96, -0.79]], [[-13.55, 9.96], [7.63, 30.29], [17.56, -4.92], [20.54,27.77], [5.96, 20.87], [20.5, 17.25], [10.9, 9.58], [-5.99, 31.41], [13.4, 26.65], [-4.05, 0.14]], [[-11.88, 9.73], [9.96, 30.78], [18.86, -4.66], [23.3, 27.53], [8.63, 21.28], [21.09, 17.13], [12.39, 10.06], [-4.03, 31.65], [16.59, 25.45], [-3.02, 0.88]], [[-10.25, 9.41], [11.81, 31.3], [20.03, -4.77], [25.59, 27.36], [11.31, 20.58], [22.83, 15.68], [13.89, 10.0], [-2.41, 31.74], [18.55, 24.32], [-1.89, 1.19]], [[-8.65, 9.0], [13.35, 31.43], [20.89, -5.36], [27.37, 26.91], [13.88, 19.05], [25.48, 13.49], [15.18, 9.09], [-0.96, 31.54], [19.11, 23.2], [-0.87, 0.91]]]
columns=['x1','y1','x2','y2','x3','y3','x4','y4','x5','y5','x6','y6','x7','y7','x8','y8','x9','y9','x10','y10']
#df = pd.DataFrame(columns=columns, data=formations)
X = np.array(formations)
print('shaping')
nsamples, nx, ny = X.shape
print(nsamples,nx,ny)
d2_train_dataset = X.reshape((nsamples,nx*ny))
df = pd.DataFrame( data=d2_train_dataset)
print(df)
print(df.mean())

quit()
df = pd.DataFrame(data=formations)
print(df)

quit()






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