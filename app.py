import io
import base64
import os.path

import dash
import dash_resumable_upload
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from start_analysis import start_analysis
from tacticon.Pitch import Pitch

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

dash_resumable_upload.decorate_server(app.server, "uploads")

team_list=['Deutschland','Niederlande']

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

app.layout = html.Div(
    id='container',
    children=[
        # Banner
        html.Div(
            id="banner",
            className="banner",
            children=[html.Img(src=app.get_asset_url("DFB-Logo.png")),
                        html.Img(src=app.get_asset_url("Uni-Logo.png")),
                        html.Img(src=app.get_asset_url("ISS-Logo.png"))],
        ),
        html.Div([
            dash_resumable_upload.Upload(
                id='upload',
                maxFiles=1,
                maxFileSize=1024*1024*1000,  # 100 MB
                service="/upload_resumable",
                #textLabel="Drag and Drop Here to upload!",
                startButton=False,
                pauseButton=False,
                cancelButton=False,
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                defaultStyle={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                activeStyle={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'solid',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                # Allow multiple files to be uploaded
                #multiple=True
            )
        ]),
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
                        html.Img(id='pitch'),
                    ],
                ),
                # Patient Wait time by Department
                html.Div(
                    id="wait_time_card",
                    children=[
                        html.B("Patient Wait Time and Satisfactory Scores"),
                        html.Hr(),
                        html.Div(id="wait_time_table"),
                    ],
                ),
            ],
        ),
        html.Div(id='output'),
    ]
)
    


@app.callback(Output('pitch', 'src'),
              [Input('upload', 'fileNames')])

def display_files(fileNames):
    if fileNames is not None:
        print(fileNames)
        path = os.path.dirname(__file__) + '/../uploads/' + fileNames[0]
        print(path)
        formations=start_analysis(path, 120, 'DFL-CLU-000N99')

        Pitch("#195905","#faf0e6")
        for player in formations[0]:
            plt.scatter(player[0], player[1], c='red', zorder=10)
        buf = io.BytesIO() # in-memory files
        plt.savefig(buf, format = "png") # save to the above file object
        data = base64.b64encode(buf.getbuffer()).decode("utf8") # encode to html elements
        plt.close()
        return "data:image/png;base64,{}".format(data)
        #return html.Ul(html.Li(fileNames))
    #return html.Ul(html.Li("No Files Uploaded Yet!"))


if __name__ == '__main__':
    app.run_server(debug=True)