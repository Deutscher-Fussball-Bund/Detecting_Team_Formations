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
    return [mean(x_pos),mean(y_pos)]

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

### [[[-21.236895403064622, -4.544330446369087, -3.240826115922718], [-16.881978680879413, -13.246682211858761, 9.312365089940041]]
##->[[[-21...,-16..],[...]]] 
def extract_formations(array):
    print(array)
    print(array[0])
    quit()

    formations=[]
    #for player in array: