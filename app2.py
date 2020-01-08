import io
import base64
import os.path

import dash
import dash_resumable_upload
import dash_html_components as html
from dash.dependencies import Input, Output


from tacticon.RawEventDataReader import RawEventDataReader
import xml.etree.ElementTree as ET

from plotly.tools import mpl_to_plotly
import dash_core_components as dcc
from tacticon.Pitch import Pitch

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt

import numpy as np


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

dash_resumable_upload.decorate_server(app.server, "uploads")

#n = 50
#x, y, z, s, ew = np.random.rand(5, n)
#c, ec = np.random.rand(2, n, 4)
#area_scale, width_scale = 500, 5

#fig, ax = plt.subplots()
#sc = ax.scatter(x, y, c=c,
#                s=np.square(s)*area_scale,
#                edgecolor=ec,
#                linewidth=ew*width_scale)
#ax.grid()

#plotly_fig = mpl_to_plotly(fig)

app.layout = html.Div([
    dash_resumable_upload.Upload(
        id='upload',
        maxFiles=1,
        maxFileSize=1024*1024*1000,  # 100 MB
        service="/upload_resumable",
        #textLabel="Drag and Drop Here to upload!",
        startButton=False,
        pauseButton=False,
        cancelButton=False,
        defaultStyle={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        }
        # Allow multiple files to be uploaded
        #multiple=True
    ),

    #dcc.Graph(id='myGraph', figure=plotly_fig),

    html.Div(id='output'),

    html.Img(id='example')
])


@app.callback(Output('example', 'src'),
              [Input('upload', 'fileNames')])

def display_files(fileNames):
    Pitch("#195905","#faf0e6")
    buf = io.BytesIO() # in-memory files
    plt.savefig(buf, format = "png") # save to the above file object
    data = base64.b64encode(buf.getbuffer()).decode("utf8") # encode to html elements
    plt.close()
    return "data:image/png;base64,{}".format(data)


    if fileNames is not None:
        print(fileNames)
        path = os.path.dirname(__file__) + '/../uploads/' + fileNames[0]
        print(path)
        event_data = RawEventDataReader(path)
        
        for player in event_data.xml_root.iter('FrameSet'):
                print(player.get('PersonId'))


        return html.Ul(html.Li(fileNames))
    return html.Ul(html.Li("No Files Uploaded Yet!"))


if __name__ == '__main__':
    app.run_server(debug=True)

    app.layout = html.Div(
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Tab one', value='tab-1'),
        dcc.Tab(label='Tab two', value='tab-2'),
    ]),
    html.Div(
        id='tabs-content',
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
                            html.Img(id='pitch')
                        ],
                    )
                ],
            )
        ]
    )
)