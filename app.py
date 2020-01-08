import io
import base64
import os.path

import dash
import dash_resumable_upload
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from scripts.start_analysis import start_analysis
from scripts.tacticon.Pitch import Pitch

from dashboard.tab_one import create_tab_one

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

dash_resumable_upload.decorate_server(app.server, "uploads")

app.layout = html.Div([
    html.Div(
        id="banner",
        className="banner",
        children=[html.Img(src=app.get_asset_url("DFB-Logo.png")),
                    html.Img(src=app.get_asset_url("Uni-Logo.png")),
                    html.Img(src=app.get_asset_url("ISS-Logo.png"))],
    ),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Analytics Dashboard', value='tab-1'),
        dcc.Tab(label='Upload', value='tab-2'),
    ]),
    html.Div(id='tabs-content')
])





@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return create_tab_one()
    elif tab == 'tab-2':
        return html.Div([
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
            ])
        ])


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