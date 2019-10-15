class Ball:
  """
  A ball object.
  Args:
      df (pd.dataframe): From EventDataReader
      frame_number (int): Beginning from 10000
  Attributes:
      X:
      Y:
      Z:
      D:
      A:
      S:
      M:
      BallStatus:
      BallPossession:
      T:
      N:
      ID: (Default is None). Doesn't have to be passed, but can be useful.
  Usage:        
      b1 = Ball(df=ball_df,frame_number=170495).X
      b2 = Ball(df=ball_df,frame_number=170496).X
  """

  def __init__(self,df,frame_number=10000,ID=None):
    self.full_df = df

    # Get the row of the frame number
    df =df.loc[df['N'] == frame_number]
    # Then extract the cell for each attribute
    self.X = df['X'].iloc[0]
    self.Y = df['Y'].iloc[0]
    self.Z = df['Z'].iloc[0]
    self.D = df['D'].iloc[0]
    self.A = df['A'].iloc[0]
    self.S = df['S'].iloc[0]
    self.M = df['M'].iloc[0]
    self.BallStatus = df['BallStatus'].iloc[0]
    self.BallPossession= df['BallPossession'].iloc[0]
    self.T = df['T'].iloc[0]
    self.N = df['N'].iloc[0]
    self.ID = str(ID)

  def number_of_frames(self):
      """
      Return the number of frames
      """
      return len(self.full_df.index)

  def mean(self,col):
      """
      Return the mean value for all the frames
      Args:
        col (str): Attribute to get the mean on
      """
      return self.full_df[f"{col}"].mean()