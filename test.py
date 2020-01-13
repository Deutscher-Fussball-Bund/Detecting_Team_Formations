from minisom import MiniSom    

data = [[ 0.80,  0.55,  0.22,  0.03],
        [ 0.82,  0.50,  0.23,  0.03],
        [ 0.80,  -0.54,  0.22,  -0.03],
        [ -0.80,  0.53,  -0.26,  0.03],
        [ 0.79,  -0.56,  0.22,  -0.03],
        [ -0.75,  0.60,  -0.25,  0.03],
        [ 0.77,  0.59,  0.22,  0.03]] 

print('MiniSom wird erstellt.')
som = MiniSom(4, 10, 4, sigma=0.3, learning_rate=0.5) # initialization of 6x6 SOM
print('Erstellung abgeschlossen.')
print('Training beginnt.')
som.train_random(data, 100) # trains the SOM with 100 iterations
print('Training abgeschlossen.')
#print(som.get_weights())
print('')
print(som.win_map(data))