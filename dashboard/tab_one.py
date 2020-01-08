import dash
import dash_resumable_upload
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

team_list=['Deutschland','Niederlande']

def create_tab_one():
    return html.Div([
            # Left column
            html.Div(
                id="left-column",
                className="four columns",
                children=[description_card(), generate_control_card()]
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
                            html.B("Game Situation"),
                            html.Hr(),
                            html.Img(id='pitch')
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

def generate_control_card():
    """
    :return: A Div containing controls for graphs.
    """
    return html.Div(
        id="control-card",
        children=[
            html.P("Select Team"),
            dcc.Dropdown(
                id="team-select",
                options=[{"label": i, "value": i} for i in team_list],
                value=team_list[0],
            ),
            html.Br(),
            html.P("Select Time Window"),
            dcc.RangeSlider(
                count=1,
                min=0,
                max=90,
                step=0.5,
                value=[0, 90]
            ),  
            html.Br(),
            html.Br(),
            html.P("Select Time Frame"),
            dcc.Input(
                placeholder='Enter a value...',
                type='text',
                value=''
            ),  
            html.Br(),
            html.Div(
                id="reset-btn-outer",
                children=html.Button(id="reset-btn", children="Reset", n_clicks=0),
            ),
        ],
    )