import pandas as pd
import xml.etree.ElementTree as ET
import numpy as np


class RawEventDataReader:
  """
  Reads in large XML files that contain the raw event information for a match,
  for each object.
  Args:
    xml file
  Usage example for ball:
    event_data = RawEventDataReader.RawEventDataReader(xml_file)
    ball_columns=["X","Y","Z","D","A","S","M","BallStatus","BallPossession","T","N"]
    ball_df = event_data.create_ball_dataframe(ball_columns)
  Returns:
    pd.DataFrame of object requested.
  """

  def __init__(self,xml_file):
    self.xml_root = self._load_data(xml_file)

  def _load_data(self,xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    return root

  def create_ball_dataframe(self,df_cols):
    """
    Create a ball dataframe from the xml inputs.
    Args:
        df_cols (list): The column names
    Note:
        Available columns are
        ["X","Y","Z","D","A","S","M","BallStatus","BallPossession","T","N"]
    Returns:
        pd.dataframe
    """
    rows = []
    # Get all nodes regarding the ball
    for frameset in self.xml_root.iterfind(f".//FrameSet[@TeamId='BALL']/*"):
        res=[]
        for c in df_cols:
            value = frameset.attrib.get(c)
            if c=="T":
                res.append(value)
            else:
                res.append(float(value))
        rows.append(res)

    out_df = pd.DataFrame(rows,columns=df_cols)
    return out_df

  def create_player_dataframe(self,df_cols,obj):
    """
    Create a player dataframe from the xml inputs.
    Args:
        df_cols (list): The column names
        obj (str): The player objects ID
    Note:
        Available columns are
        ["X","Y","D","A","S","M","T","N"]
    Returns:
        pd.dataframe
    """
    rows = []
    # Get all frames regarding the object
    for frameset in self.xml_root.iterfind(f".//FrameSet[@PersonId='{obj}']/*"):
        res=[]
        for c in df_cols:
            value = frameset.attrib.get(c)
            if c=="T":
                res.append(value)
            else:
                res.append(float(value))
        rows.append(res)

    out_df = pd.DataFrame(rows,columns=df_cols)
    return out_df