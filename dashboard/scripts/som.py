from minisom import MiniSom
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

"""data = [[ 0.80,  0.55,  0.22,  0.03],
        [ 0.82,  0.50,  0.23,  0.03],
        [ 0.80,  -0.54,  0.22,  -0.03],
        [ -0.80,  0.53,  -0.26,  0.03],
        [ 0.79,  -0.56,  0.22,  -0.03],
        [ -0.75,  0.60,  -0.25,  0.03],
        [ 0.77,  0.59,  0.22,  0.03],
        [ 0.67,  0.69,  0.23,  0.04]]"""

def do_som(data):
    print('MiniSom wird erstellt.')
    som = MiniSom(10, 10, 20, sigma=1, learning_rate=0.2) # initialization of 6x6 SOM
    print('Erstellung abgeschlossen.')
    print('Training beginnt.')
    som.train_random(data, 100000, True) # trains the SOM with 100 iterations
    print('Training abgeschlossen.')
    #print(som.get_weights())
    print('')
    print('win_map')
    
    #array=[]
    #for i in range(0,10):
    #    arr=[]
    #    print(i)
    #    for j in range(0,10):
    #        arr.append(0)
    #    array.append(arr)
    #for cluster in tqdm(som.win_map(data)):
    #    array[cluster[0]][cluster[1]]=len(som.win_map(data)[cluster])
        #print(som.win_map(data)[cluster])
        #print(cluster)
        #print()
        
    #print(array)
    #plt.imshow(array, cmap='Blues', interpolation='nearest')
    #plt.show()
    #quit()

    print('')
    print('distance map')
    print(som.distance_map())

    plt.imshow(som.distance_map(), cmap='Blues', interpolation='nearest')
    plt.show()

    print('')
    print('activation_response')
    #print(som.activation_response(data))

    plt.imshow(som.activation_response(data), cmap='Blues', interpolation='nearest')
    plt.show()

    print(som.activation_response(data))

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