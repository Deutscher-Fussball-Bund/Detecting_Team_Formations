from DataReader import DataReader
import pandas as pd
from Player import Player
from Ball import Ball
from lxml import etree

from RawEventDataReader import RawEventDataReader
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import networkx as nx
import ciso8601
import time
from tqdm import tqdm
import math

class Team:
    """
    A team object
    Returns: 
      pd.dataframe: a team data frame at a given frame.
    """

    def __init__(self,raw_file,half):
        xml_positions = etree.parse(raw_file)
        self.positions = self.create_team_dataframe(xml_positions,half)

    def create_team_dataframe(self,xml_positions, half='firstHalf'):
        """Returns a dataframe with the tracking (position: x, y, z) of all players + the ball
        
        Dropping rows where ball positions is NAN
        +-------+-----------+-----------+
        |       |   BALL    |  TeamId   |
        +       +-----------+-----------+
        |       |  BallId   | PlayerId  |
        + N | T +---+---+---+---+---+---+
        |       | X | Y | Z | X | Y | A |
        +=======+===+===+===+===+===+===+
        | 0 | 0 |123|456|789|012|456|789|
        +-------+-----------+-----------+
        :param xml_positions: the parsed xml tracking data (lxml object)
        :param half: the description of the half: either "firstHalf" or "secondHalf", etc.
        :return: a dataframe containing the tracking data: position of all players and the ball
        """
        def change_type(df, frameset):
            """
            change type of columns
            different columns names and tpyes for the ball and for the rest of the players
            """
            if frameset.attrib.get('TeamId') == 'BALL':
                return df.astype(
                    # change types of columns for the ball
                    dtype={
                        'A':float, 
                        'D':float, 
                        'M':int, 
                        'N':int, 
                        'S':float, 
                        'X':float, 
                        'Y':float,
                        'Z':float,
                        #'T':'datetime64[ns]', # this breaks the timezone
                        'BallPossession':int, 
                        'BallStatus':int,
                    }, 
                    errors='raise'
                )
            else:
                return df.astype(
                    # change types of columns for the players
                    dtype={
                        'A':float, 
                        'D':float, 
                        'M':int, 
                        'N':int, 
                        'S':float, 
                        'X':float, 
                        'Y':float,
                        #'T':'datetime64[ns]', # this breaks the timezone
                    }, 
                    errors='raise'
                )
        

        def create_columns(df, frameset):
            """A utility function to create a multiindex columns"""
            person_id = frameset.attrib.get('PersonId')
            team_id = frameset.attrib.get('TeamId')
            df.columns = pd.MultiIndex.from_product(
                [[team_id], [person_id], df.columns],
                names=['TeamId', 'PersonId', 'Position']
            )
            return df

        tracking_players = pd.concat([
            pd.DataFrame.from_records(
                [dict(frame.attrib) for frame in frameset.getchildren()]
            ).pipe(change_type, frameset=frameset)
             .set_index(['N', 'T'])
             .pipe(create_columns, frameset=frameset)
            for frameset in xml_positions.xpath(F'//Positions/FrameSet[@GameSection = "{half}"]')
        ], axis=1, sort=False)
        
        # this is casting the 'T' values in the index to datetime with the correct time zone
        tracking_players.index.set_levels(pd.to_datetime(tracking_players.index.get_level_values(1)), level=1, inplace = True)

        return tracking_players


    def return_df(self):
        return self.positions