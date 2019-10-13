import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import pickle

class Pitch:
    """
    Code to draw a football pitch.
    Largely from http://petermckeever.com/2019/01/plotting-xy-football-data-in-python/
    Args:
      pitch (str): Hex colour of the pitch
      line (str): Hex colour of the lines
    TODO:
      Get the correct dimensions automatically and set them as class attributes.
      Uses 105 x 68 meters currently.
    """



    def __init__(self,pitch,line):

        self.LENGTH =105
        self.WIDTH = 68

        self.x_center=0
        self.y_center=0

        self.x_0=-self.LENGTH/2
        self.x_1=self.LENGTH/2
        self.y_0=-self.WIDTH/2
        self.y_1=self.WIDTH/2

        self.fig,self.ax = plt.subplots(figsize=(10.4,6.8))

        self.draw_pitch(pitch, line)


    def draw_pitch(self,pitch, line):
        '''
        Call this method to draw the actual pitch. Once called, other 
        objects can be added to the canvas just by calling matplotlib plt.
        '''

        line = line
        pitch = pitch


        # fig,ax = plt.subplots(figsize=(10.4,6.8))
        plt.xlim(self.x_0-1,self.x_1+1)
        plt.ylim(self.y_0-1,self.y_1+1)


        self.ax.axis('on') # this hides the x and y ticks

        # side and goal lines #
        ly1 = [self.y_0,self.y_0,self.y_1,self.y_1,self.y_0]
        lx1 = [self.x_0,self.x_1,self.x_1,self.x_0,self.x_0]

        plt.plot(lx1,ly1,color=line,zorder=5)


        # boxes, 6 yard box and goals

            #outer boxes#
        ly2 = [self.y_0+13.84,self.y_0+13.84,self.y_0+54.16,self.y_0+54.16]
        lx2 = [self.x_1,self.x_0+87.5,self.x_0+87.5,self.x_1]
        plt.plot(lx2,ly2,color=line,zorder=5)

        ly3 = [self.y_0+13.84,self.y_0+13.84,self.y_0+54.16,self.y_0+54.16]
        lx3 = [self.x_0,self.x_0+16.5,self.x_0+16.5,self.x_0]
        plt.plot(lx3,ly3,color=line,zorder=5)

            #goals#
        ly4 = [self.y_0+30.34,self.y_0+30.34,self.y_0+37.66,self.y_0+37.66]
        lx4 = [self.x_1,self.x_1+.2,self.x_1+.2,self.x_1]
        plt.plot(lx4,ly4,color=line,zorder=5)

        ly5 = [self.y_0+30.34,self.y_0+30.34,self.y_0+37.66,self.y_0+37.66]
        lx5 = [self.x_0,self.x_0+(-0.2),self.x_0+(-0.2),self.x_0]
        plt.plot(lx5,ly5,color=line,zorder=5)


           #6 yard boxes#
        ly6 = [self.y_0+24.84,self.y_0+24.84,self.y_0+43.16,self.y_0+43.16]
        lx6 = [self.x_1,self.x_0+99.5,self.x_0+99.5,self.x_1]
        plt.plot(lx6,ly6,color=line,zorder=5)

        ly7 = [self.y_0+24.84,self.y_0+24.84,self.y_0+43.16,self.y_0+43.16]
        lx7 = [self.x_0+0,self.x_0+4.5,self.x_0+4.5,self.x_0+0]
        plt.plot(lx7,ly7,color=line,zorder=5)

        #Halfway line, penalty spots, and kickoff spot
        ly8 = [self.y_0,self.y_1]
        lx8 = [self.x_center,self.x_center]
        plt.plot(lx8,ly8,color=line,zorder=5)


        plt.scatter(self.x_0+93,self.y_center,color=line,zorder=5)
        plt.scatter(self.x_0+11,self.y_center,color=line,zorder=5)
        plt.scatter(self.x_center,self.y_center,color=line,zorder=5)

        circle1 = plt.Circle((self.x_0+93.5,self.y_center), 9.15,ls='solid',lw=1.5,color=line, fill=False, zorder=1,alpha=1)
        circle2 = plt.Circle((self.x_0+10.5,self.y_center), 9.15,ls='solid',lw=1.5,color=line, fill=False, zorder=1,alpha=1)
        circle3 = plt.Circle((self.x_center, self.y_center), 9.15,ls='solid',lw=1.5,color=line, fill=False, zorder=2,alpha=1)

        ## Rectangles in boxes
        rec1 = plt.Rectangle((self.x_0+87.5,self.y_0+20), 16,30,ls='-',color=pitch, zorder=1,alpha=1)
        rec2 = plt.Rectangle((self.x_0+0, self.y_0+20), 16.5,30,ls='-',color=pitch, zorder=1,alpha=1)

        ## Pitch rectangle
        rec3 = plt.Rectangle((self.x_0, self.y_0), self.LENGTH,self.WIDTH,ls='-',color=pitch, zorder=1,alpha=1)

        self.ax.add_artist(rec3)
        self.ax.add_artist(circle1)
        self.ax.add_artist(circle2)
        self.ax.add_artist(rec1)
        self.ax.add_artist(rec2)
        self.ax.add_artist(circle3)


if __name__ == '__main__':
    players = []

    with open('playerPositionsFH.pkl', 'rb') as input:
        playerPositionsFH = pickle.load(input)
    with open('playerPositionsSH.pkl', 'rb') as input:
        playerPositionsSH = pickle.load(input)

    # Intersection to find out which player played in both halftimes
    fhSet = set(playerPositionsFH)
    shSet = set(playerPositionsSH)
    for playerId in fhSet.intersection(shSet):
        if (playerPositionsFH[playerId].get('TeamId') != 'DFL-CLU-000N99'):
            continue
        name = playerPositionsFH[playerId].get('Name')
        x1 = playerPositionsFH[playerId].get('meanX')
        x2 = playerPositionsSH[playerId].get('meanX') * -1
        y1 = playerPositionsFH[playerId].get('meanY')
        y2 = playerPositionsSH[playerId].get('meanY') * -1
        players.append([name, (x1,y1), (x2,y2)])


    Pitch("#195905","#faf0e6")
    for player in players:
        plt.annotate(player[0], xy=player[1], xytext=player[2], arrowprops=dict(arrowstyle="->"), zorder=10)
    plt.show()
    
    
