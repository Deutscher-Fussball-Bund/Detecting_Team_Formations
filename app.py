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
from dashboard.tab_two import create_tab_two
from dashboard.file_management import new_match

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

dash_resumable_upload.decorate_server(app.server, "./uploads")

app.layout = html.Div([
    html.Div(
        id="banner",
        className="banner",
        children=[html.Img(src=app.get_asset_url("Uni-Logo.png")),
                    html.Img(src=app.get_asset_url("ISS-Logo.png")),
                    html.Img(src=app.get_asset_url("DFB-Logo.png"))],
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
        return create_tab_two()
    

@app.callback(Output('another-column', 'children'),
                [Input('upload', 'fileNames')])
def display_files(fileNames):
    if fileNames is not None:
        new_match(fileNames)

if __name__ == '__main__':
    app.run_server(debug=True)