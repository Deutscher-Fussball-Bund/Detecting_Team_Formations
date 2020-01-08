import numpy as np

from statistics import mean

def combine_xy(array, color):
    x_pos=[]
    y_pos=[]
    player_positions=[]
    for player in array:
        x_pos.append(player[0][0])
        y_pos.append(player[1][0])
    player_positions.append([x_pos,y_pos,color])
    return player_positions

def get_mean(array):
    x_pos=[]
    y_pos=[]
    for player in array:
        x_pos.append(player[0])
        y_pos.append(player[1])
    return np.array([mean(x_pos),mean(y_pos)])

def move_formation(team_mean, formations):
    for key in formations:    
        x_pos=[]
        y_pos=[]
        for player in formations[key]:
            x_pos.append(player[0])
            y_pos.append(player[1])
        
        array_mean=[[mean(x_pos)],[mean(y_pos)]]
        dif_x=team_mean[0] - array_mean[0]
        dif_y=team_mean[1] - array_mean[1]
        
        for player in formations[key]:
            player[0] += dif_x
            player[1] += dif_y
        
    return formations

def move_formations_to_centre_spot(formations):
    for formation in formations:    
        x_pos=[]
        y_pos=[]
        for player in formation:
            x_pos.append(player[0])
            y_pos.append(player[1])
        
        array_mean=[mean(x_pos),mean(y_pos)]
        dif_x=0 - array_mean[0]
        dif_y=0 - array_mean[1]
        
        for player in formation:
            player[0] += dif_x
            player[1] += dif_y
        
    return formations

### [[[-21.236895403064622, -4.544330446369087, -3.240826115922718], [-16.881978680879413, -13.246682211858761, 9.312365089940041]]
##->[[[-21...,-16..],[...]]] 
def extract_formations(arr):
    print('')
    print('arr', arr)
    l=len(arr[0][0])
    print('')
    print(l)
    i=0

    formations=[]
    while i<l:
        formation=[]
        for player in arr:
            print('')
            print('player',player)
            print('')
            print('i',i)
            print(player[0][i])
            print(player[1][i])
            player_position=[player[0][i],player[1][i]]
            formation.append(player_position)
        formations.append(formation)
        i += 1
    
    return formations


""" [
    [
        [-11.168124861141969, 3.0377827149522325, 8.531057542768272, 7.249793379249055, 24.927562763830263, -0.32714952232837147, 6.768391468562541, -11.01005998666963, 0.6164741168629193, -4.444541213063765, 13.60315263274828, -13.422057320595423, -5.393165963119307, 6.628073761386359, 10.11243723616974, 7.043333333333333, nan, nan, nan, nan, -11.626151966229724, 12.71401466340813, 14.904294601199732, -4.900217729393469, -5.6749255720950895, 5.736931792934905, -13.25761386358587, 15.439922239502332, 23.514936680737613, 6.754405687624972, -0.2042457231726294, 2.732566096423017, 29.95491890690957, 16.443341479671187, 27.91149744501222, 19.700710953121526, 17.50111111111111], [2.9362097311708504, -5.558347033992447, -2.380486558542546, -1.0900133303710289, -4.096463008220396, -2.0073605865363255, -2.7996000888691404, -12.050622083981336, 2.9862541657409465, 3.21980004443457, -5.877476116418574, 7.2426682959342354, -1.7416396356365254, -2.2397422794934454, -4.761419684514552, 0.2069753086419753, nan, nan, nan, nan, -12.437538324816707, 2.1759786714063543, -4.078935792046212, 9.583297045101089, 0.31849366807376167, -3.667340590979782, 3.1437258387025104, -6.9461786269717845, 10.475927571650747, -2.4580648744723397, 4.601390802043991, -0.5425261053099315, -5.761306376360809, 1.807973783603643, -0.5162919351255278, 2.4320595423239277, -1.1839784946236565]
    ],[
        [-14.212500575108415, -1.0152192519638876],
        [-17.705469846957214, -17.604109899558367]
    ],[
        [-8.676578764083118],
        [18.245719248484733]
    ],[
        [-17.994943614533355],
        [-1.6882642578020368]
    ],[
        [-16.333814425359385],
        [-12.666618585345898]
    ],[
        [-8.928788825306112],
        [-4.116479955747624]
    ],[
        [-1.4991552323157369],
        [0.1246911344546966]
    ],[
        [-17.43849053641016],
        [9.925618752657034]
    ],[
        [-2.1305821568814656],
        [2.037063071715479]
    ], [[-7.786701222367628], [5.200536783506336]], [[7.8527971439749615], [-6.17273024256651]], [[5.520925208845208], [2.8349910565110563]], [[17.190711212351303], [1.0673076436345228]]] """