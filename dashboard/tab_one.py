import json

import dash
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bio as dashbio

from dashboard.file_management import get_match_list,get_team_list
import plotly.graph_objects as go

tabs_styles = {
    'height': '36px',
    'width': '256px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '5px',
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '5px',
    'fontWeight': 'bold'
}


def create_tab_one():
    return html.Div([
            # Left column
            html.Div(
                id="left-column",
                className="three columns",
                children=[dcc.Tabs(id="column-tabs", value='column-tab-1',
                    children=[
                        dcc.Tab(label='Info', value='column-tab-1', style=tab_style, selected_style=tab_selected_style),
                        dcc.Tab(label='Team 1', value='column-tab-2', style=tab_style, selected_style=tab_selected_style),
                        dcc.Tab(label='Team 2', value='column-tab-3', style=tab_style, selected_style=tab_selected_style),
                    ], style=tabs_styles),
                    html.Div(id='column-tabs-content')]
            ),
            # Right column
            html.Div(
                id="right-column",
                className="nine columns",
                children=[
                    html.Div(
                        id="football pitch",
                        children=[
                            html.Br(),
                            dcc.Loading(id="loading-1", type="default",
                                children=[
                                    html.Div(id='loading-analytics')
                                    ]
                            ),
                            html.Div(children=[
                                html.Div(id='graph1'),
                                html.Div(id='graph2'),
                                html.Div(id='graph3'),
                                html.Div(id='graph4')
                            ]),
                            html.Br()
                        ],
                    )
                ]
            )
        ])






def create_column_tab_one():
    """
    :return: A Div containing dashboard title & descriptions.
    """
    match_list=get_match_list()
    return html.Div(
        id="description-card",
        children=[
            html.H5("Football Game Analytics"),
            html.H3("Welcome to the Tactical Analytics Dashboard"),
            html.Div(
                id="intro",
                children="Explore tactical orientation of football teams during various game phases.",
            ),
            html.Div(
                id="match-card",
                children=[
                    html.Br(),
                    html.H6("Select Match"),
                    dcc.Dropdown(
                        id="match-select",
                        options=[{"label": i[0], "value": i[1]} for i in match_list],
                        style = dict(width = '20em')
                    )
                ]
            )
        ],
    )


def create_column_tab_two(match_id):
    """
    :return: A Div containing controls for graphs.
    """
    if match_id is None:
        return html.H6("Please select a match in the Info Tab")
    team_list=get_team_list(match_id)
    return html.Div(
        id="control-card",
        children=[
            html.Br(),
            html.H6("Select Team"),
            dcc.Dropdown(
                id="team-select",
                options=[{"label": i[0], "value": i[1]} for i in team_list],
                style = dict(width = '20em')
            ),
            html.Div(id='match-settings')
        ]
    )

def create_column_tab_three(match_id):
    """
    :return: A Div containing controls for graphs.
    """
    if match_id is None:
        return html.H6("Please select a match in the Info Tab")
    team_list=get_team_list(match_id)
    return html.Div(
        id="control-card",
        children=[
            html.Br(),
            html.H6("Select Team"),
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
            html.H6("Select Time Window"),
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
            html.Br(),
            html.H6("Select Time Frame Size"),
            daq.NumericInput(
                id='time-input',
                min=0,
                value=10,
                max=120
            ),
            html.Br(),
            html.H6(id='ex_secs',children=['Exclude Seconds After Possession Change']),
            daq.NumericInput(
                id='ex_secs-input',
                min=0,
                value=1,
                max=10
            ),
            html.Br(),
            html.H6("Ball Possession Phase"),
            dcc.RadioItems(
                id='possession-radio',
                options=[
                    {'label': 'Ball possession', 'value': 'bp'},
                    {'label': 'No ball possession', 'value': 'nbp'},
                    {'label': 'Both', 'value': 'bo'}
                ],
                value='bo'
            ),
            html.Br(),
            html.Div(
                id="start-btn-outer",
                children=html.Button(id="start-btn", children="Go"),
            )
        ]
    )