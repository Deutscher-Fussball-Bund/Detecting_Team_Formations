import io
import base64
import os.path
import math
import json
import time

import dash
import dash_resumable_upload
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import plotly.graph_objects as go

from dashboard.tab_one import create_tab_one,add_match_settings,create_column_tab_one,create_column_tab_two,create_column_tab_three
from dashboard.tab_two import create_tab_two,create_second_upload,create_right_column
from dashboard.file_management import new_match,move_match,delete_selected_rows,load_team_df
from dashboard.pitch import draw_pitch,setup_pitch1,setup_pitch2,setup_timeline1,setup_timeline2,add_formation

from dashboard.scripts.start_analysis import start_analysis


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

dash_resumable_upload.decorate_server(app.server, "./uploads")

app.layout = html.Div([
    dcc.Store(id='memory'),
    html.Div(id='dummy', style={'display': 'none'}),
    dcc.Location(id='url', refresh=False),
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



############ Callbacks ############

### Callback for Navigation ###
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return create_tab_one()
    elif tab == 'tab-2':
        return create_tab_two()


### Callsbacks for File Management ###
# Matchinfo upload
@app.callback(Output('another-column', 'children'),
                [Input('upload_matchinfo', 'contents')],
                [State('upload_matchinfo', 'filename')])
def upload_matchinfo(contents,filename):
    if contents is not None:
       return create_second_upload(new_match(filename, contents))


# Positional data upload
@app.callback(Output('yet-another-column', 'children'),
                [Input('upload_position', 'fileNames')])
def upload_positions(fileNames):
    if fileNames is not None:
        move_match(fileNames)


# Delete Matches
@app.callback(Output('right_column', 'children'),
                [Input('button', 'n_clicks')],
                [State('datatable', 'selected_rows')]
)
def delete_rows(n_clicks,selected_rows):
    if selected_rows is not None and n_clicks is not None:
        delete_selected_rows(selected_rows)
    return create_right_column()


### Callbacks for Analytics Dashboard ###
# Navigation
@app.callback(Output('column-tabs-content', 'children'),
              [Input('column-tabs', 'value')],
              [State('dummy', 'children')])
def render_column_content(tab,match_id):
    if tab == 'column-tab-1':
        return create_column_tab_one()
    elif tab == 'column-tab-2':
        return create_column_tab_two(match_id)
    elif tab == 'column-tab-3':
        return create_column_tab_three(match_id)


## Tab Info ##
# Select Match
@app.callback(Output('dummy', 'children'),
                [Input('match-select','value')])
def match_selected(value):
    if value is not None:
        return value


## Tab Team 1/2 ##
# Select Team
@app.callback(Output('match-settings', 'children'),
                [Input('team-select', 'value')])
def display_settings(value):
    if value is not None:
        return add_match_settings()


# Updated displayed Slider Values
@app.callback(Output('slider-output-container', 'children'),
                [Input('slider-window', 'value')])
def display_value(value):
    return 'Minute Start: {} | \
            Minute End: {}'.format(value[0], value[1])


# Start Analysis
@app.callback([Output('versuch','children'),
                Output('graph1', 'children'),
                Output('graph2','children'),
                Output('graph4', 'children'),
                Output('graph3','children'),
                Output('memory', 'data')],
                [Input('start-btn', 'n_clicks')],
                [State('dummy','children'),
                State('team-select', 'value'),
                State('slider-window', 'value'),
                State('time-input', 'value'),
                State('possession-radio', 'value'),
                State('ex_secs-input','value'),
                State('column-tabs', 'value'),
                State('memory', 'data'),
                State('graph1', 'children'),
                State('graph2','children'),
                State('graph3', 'children'),
                State('graph4','children')])
def check_values(n_clicks,match_id,team_id,value_slider,time_intervall,possession,sapc,tab,data,graph1,graph2,graph3,graph4):
    if n_clicks is not None:
        print('')

        print('Analyse wurde gestartet:', match_id,team_id,value_slider,time_intervall,possession,sapc)
        team_df,signs = load_team_df(match_id,team_id)
        result,avg_formation,hd_min,formations,hd_mins = start_analysis(team_df,signs,match_id,team_id,time_intervall,possession,value_slider[0],value_slider[1],sapc)

        # Give a default data dict with 0 clicks if there's no data.
        data = data or {}

        if tab == 'column-tab-2':
            graph1=html.H6("No matching frames found.")
            graph2=html.H6("Please change your settings.")
            if  result:
                graph1=setup_timeline1(formations,hd_mins)
                graph2=setup_pitch1(avg_formation,hd_min)
                data={}
                data['avg_formation_1']=avg_formation
                data['formations_1']=formations
                data['hd_min_1']=hd_min
                data['hd_mins_1']=hd_mins
        elif tab == 'column-tab-3':
            graph3=html.H6("No matching frames found.")
            graph4=html.H6("Please change your settings.")
            if result:
                graph4=setup_timeline2(formations,hd_mins)
                graph3=setup_pitch2(avg_formation,hd_min)
                data={}
                data['avg_formation_2']=avg_formation
                data['formations_2']=formations
                data['hd_min_2']=hd_min
                data['hd_mins_2']=hd_mins
        return None, graph1, graph2, graph4, graph3, data
        

# Select Time Frame on Timeline Graph 1
@app.callback(Output('pitch-graph1','figure'),
            [Input('timeline-graph1','clickData')],
            [State('pitch-graph1', 'figure'),
            State('memory', 'data')])
def test(clickData,figure,data):
    n=int(clickData['points'][0]['x'].split('F')[1])
    new_fig=draw_pitch()
    new_fig=add_formation(data['avg_formation_1'],new_fig)
    new_fig=add_formation(data['formations_1'][n],new_fig)
    return new_fig


# Select Time Frame on Timeline Graph 2
@app.callback(Output('pitch-graph2','figure'),
            [Input('timeline-graph2','clickData')],
            [State('pitch-graph2', 'figure'),
            State('memory', 'data')])
def test2(clickData,figure,data):
    n=int(clickData['points'][0]['x'].split('F')[1])
    new_fig=draw_pitch()
    new_fig=add_formation(data['avg_formation_2'],new_fig)
    new_fig=add_formation(data['formations_2'][n],new_fig)
    return new_fig


if __name__ == '__main__':
    app.run_server(debug=True)