import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html

from dashboard.file_management import get_match_list,get_team_list

def create_tab_two():
    return html.Div([
            # Left column
            html.Div(
                id="left-column",
                className="three columns",
                children=[create_select_matches()]
            ),
            # Right column
            html.Div(
                id="right-column",
                className="nine columns",
                children=[
                    html.Br(),
                    dcc.Loading(id="loading-1", type="default",
                        children=[
                            html.Div(id='loading-clustering')
                            ]
                    ),
                    html.Div(id='clustering-graph'),
                    html.Br()
                ]
            )
        ])

def create_select_matches():
    """
    :return: A Div containing dashboard title & descriptions.
    """
    match_list=get_match_list()
    return html.Div(
        id="matches-dropdown",
        children=[
            html.H6("Select Match/Matches"),
            dcc.Dropdown(
                id="match-select-clustering",
                options=[{"label": i[0], "value": i[1]} for i in match_list],
                multi=True,
                style = dict(width = '20em')
            ),
            html.Div(
                id='settings-div'
            )
        ],
    )

def create_settings(match_ids):
    team_dict={}
    for match_id in match_ids:
        team_list=get_team_list(match_id)
        for team in team_list:
            if team[0] in team_dict:
                team_dict[team[0]]+=';'+team[1]
            else:
                team_dict[team[0]]=team[1]
    return html.Div(
        children=[
            html.Br(),
            html.H6("Select Team"),
            dcc.Dropdown(
                id="follow-team-select",
                options=[{"label": i, "value": team_dict[i]} for i in team_dict],
                style = dict(width = '20em')
            ),
            html.Br(),
            html.H6(id='ex_secs',children=['Exclude Seconds After Possession Change']),
            daq.NumericInput(
                id='ex_secs-input-clustering',
                min=0,
                value=1,
                max=10
            ),
            html.Br(),
            html.H6(id='no_cluster',children=['Number of Cluster']),
            daq.NumericInput(
                id='no_cluster-input',
                min=0,
                value=10,
                max=30
            ),
            html.Br(),
            html.H6("Ball Possession Phase"),
            dcc.RadioItems(
                id='possession-radio-clustering',
                options=[
                    {'label': 'Ball possession', 'value': 'bp'},
                    {'label': 'No ball possession', 'value': 'nbp'},
                    {'label': 'Both', 'value': 'bo'}
                ],
                value='bo'
            ),
            html.Br(),
            html.Div(
                children=html.Button(id="start-btn-clustering", children="Go"),
            )
        ]
    )