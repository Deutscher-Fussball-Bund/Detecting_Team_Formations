import dash
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output

from dashboard.file_management import get_match_list,get_team_list

team_list=['Deutschland','Niederlande']

def create_tab_one():
    return html.Div([
            # Left column
            html.Div(
                id="left-column",
                className="four columns",
                children=[description_card(), generate_match_card()]
                + [
                    html.Div(
                        ["initial child"], id="output-clientside", style={"display": "none"}
                    )
                ],
            ),
            # Right column
            html.Div(
                id="right-column",
                className="eight columns",
                children=[
                    # Patient Volume Heatmap
                    html.Div(
                        id="football pitch",
                        children=[
                            html.Br(),
                            html.B("Game Situation"),
                            html.Div(id='gr')
                        ],
                    )
                ]
            )
        ])



def description_card():
    """
    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H5("Football Game Analytics"),
            html.H3("Welcome to the Tactical Analytics Dashboard"),
            html.Div(
                id="intro",
                children="Explore tactical orientation of football teams during various game phases.",
            ),
        ],
    )


def generate_match_card():
    """
    :return: A Div containing controls for graphs.
    """
    match_list=get_match_list()
    return html.Div(
        id="match-card",
        children=[
            html.Br(),
            html.P("Select Match"),
            dcc.Dropdown(
                id="match-select",
                options=[{"label": i[0], "value": i[1]} for i in match_list],
                style = dict(width = '15em')
            ),
            html.Div(id="match-controls")
        ]
    )


def add_match_controls(match_id):
    """
    :return: A Div containing controls for graphs.
    """
    team_list=get_team_list(match_id)
    return html.Div(
        id="control-card",
        children=[
            html.Br(),
            html.Br(),
            html.P("Select Team"),
            dcc.Dropdown(
                id="team-select",
                options=[{"label": i[0], "value": i[1]} for i in team_list],
                style = dict(width = '20em')
            ),
            html.Div(id='match-settings')
        ]
    )

def add_match_settings():
    return html.Div(
        children=[
            html.Br(),
            html.P("Select Time Window"),
            dcc.RangeSlider(
                id='slider-window',
                count=1,
                min=0,
                max=90,
                step=1,
                value=[0, 90]
            ),
            html.Div(id='slider-output-container'),
            html.Br(),
            html.P("Select Time Frame Size"),
            daq.NumericInput(
                id='time-input',
                min=0,
                value=10,
                max=120
            ),
            html.Br(),
            html.Br(),
            html.P("Ball Possession Phase"),
            dcc.RadioItems(
                id='possession-radio',
                options=[
                    {'label': 'Ball possession', 'value': 'bp'},
                    {'label': 'No ball possession', 'value': 'npb'},
                    {'label': 'Both', 'value': 'bo'}
                ],
                value='bo'
            ),
            html.Br(),
            html.P(id='ex_secs',children=['Exclude Seconds After Possession Change']),
            daq.Knob(
                id='knob',
                value=3
            ),
            html.Br(),
            html.Div(
                id="start-btn-outer",
                children=html.Button(id="start-btn", children="Go"),
            ),
            html.Br()
        ]
    )