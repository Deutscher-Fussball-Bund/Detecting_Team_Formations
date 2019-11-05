def combine_xy(array, color):
    x_pos=[]
    y_pos=[]
    player_positions=[]
    for player in array:
        x_pos.append(player[0][0])
        y_pos.append(player[1][0])
    player_positions.append([x_pos,y_pos,color])
    return player_positions