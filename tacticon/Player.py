class Player:
  """
  A Player object.
  Args:
    df (pd.dataframe): From EventDataReader
    frame_number (int): Beginning from 10000
  Attributes:
      X:
      Y:
      D:
      A:
      S:
      M:
      N:
      T:
      ID: (Default is None). Doesn't have to be passed, but can be useful.
  Usage:
      p1_x = Player(player_df,frame_number=170495).X
  """

  def __init__(self, df, frame_number=10000, ID=None):
    self.full_df = df

    # Get the row of the frame number
    df = df.loc[df['N'] == frame_number]
    # Then extract the cell for each attribute
    self.X = df['X'].iloc[0]
    self.Y = df['Y'].iloc[0]
    self.D = df['D'].iloc[0]
    self.A = df['A'].iloc[0]
    self.S = df['S'].iloc[0]
    self.M = df['M'].iloc[0]
    self.T = df['T'].iloc[0]
    self.N = df['N'].iloc[0]
    self.ID = str(ID)

  def number_of_frames(self):
      """
      Return the number of frames
      """
      return len(self.full_df.index)

  def mean(self, col):
      """
      Return the mean value for all the frames
      Args:
        col (str): Attribute to get the mean on
      """
      return self.full_df[f"{col}"].mean()

  def meanFL(self, col, FIRST_FRAME, LAST_FRAME):
      """
      Return the mean value for all the frames
      Args:
        col (str): Attribute to get the mean on
      """
      df = self.full_df[(self.full_df[f"N"] >= FIRST_FRAME) & (self.full_df[f"N"] <= LAST_FRAME)]
      return df[f"{col}"].mean()
