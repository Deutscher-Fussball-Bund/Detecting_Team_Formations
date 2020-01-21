import io
import base64
import os.path
import math
import json

import dash
import dash_resumable_upload
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from dashboard.tab_one import create_tab_one,add_match_controls,add_match_settings,create_column_tab_one,create_column_tab_two,create_column_tab_three
from dashboard.tab_two import create_tab_two,create_second_upload,create_right_column
from dashboard.file_management import new_match,move_match,delete_selected_rows
from dashboard.pitch import draw_pitch,setup_pitch,setup_timeline,add_formation

from dashboard.scripts.start_analysis import start_analysis

import plotly.graph_objects as go


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

dash_resumable_upload.decorate_server(app.server, "./uploads")

app.layout = html.Div([
    dcc.Store(id='memory'),
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


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return create_tab_one()
    elif tab == 'tab-2':
        return create_tab_two()


@app.callback(Output('column-tabs-content', 'children'),
              [Input('column-tabs', 'value')])
def render_column_content(tab):
    if tab == 'column-tab-1':
        return create_column_tab_one()
    elif tab == 'column-tab-2':
        return create_column_tab_two()
    elif tab == 'column-tab-3':
        return create_column_tab_three()
    

@app.callback(Output('another-column', 'children'),
                [Input('upload_matchinfo', 'contents')],
                [State('upload_matchinfo', 'filename')])
def upload_matchinfo(contents,filename):
    if contents is not None:
       return create_second_upload(new_match(filename, contents))


@app.callback(Output('yet-another-column', 'children'),
                [Input('upload_position', 'fileNames')])
def upload_positions(fileNames):
    if fileNames is not None:
        move_match(fileNames)


@app.callback(Output('match-controls', 'children'),
                [Input('match-select','value')])
def match_selected(value):
    if value is not None:
        return add_match_controls(value)


@app.callback(Output('modal', 'style'),
              [Input('modal-close-button', 'n_clicks')])
def close_modal(n):
    if (n is not None) and (n > 0):
        return {"display": "none"}


@app.callback(Output('right_column', 'children'),
                [Input('button', 'n_clicks')],
                [State('datatable', 'selected_rows')]
)
def delete_rows(n_clicks,selected_rows):
    if selected_rows is not None and n_clicks is not None:
        delete_selected_rows(selected_rows)
    return create_right_column()


@app.callback(Output('match-settings', 'children'),
                [Input('team-select', 'value')])
def display_settings(value):
    if value is not None:
        return add_match_settings()


@app.callback(Output('slider-output-container', 'children'),
                [Input('slider-window', 'value')])
def display_value(value):
    return 'Minute Start: {} | \
            Minute End: {}'.format(value[0], value[1])


@app.callback([Output('gr', 'children'),
                Output('gr2','children'),
                Output('memory', 'data')],
                [Input('start-btn', 'n_clicks')],
                [State('match-select','value'),
                State('team-select', 'value'),
                State('slider-window', 'value'),
                State('time-input', 'value'),
                State('possession-radio', 'value'),
                State('ex_secs-input','value')]
)
def check_values(n_clicks,match_id,team_id,value_slider,time_intervall,possession,sapc):
    if n_clicks is not None:

        print('')
        print('Analyse wurde gestartet:', match_id,team_id,value_slider,time_intervall,possession,sapc)

        dirname=os.path.dirname(__file__)
        uploads_path=os.path.join(dirname, '../uploads/'+match_id)
        path=uploads_path+'/positions_raw_'+match_id+'.xml'
        info_path=uploads_path+'/matchinformation_'+match_id+'.xml'
        avg_formation,hd_min,formations,hd_mins=start_analysis(path,info_path,match_id,team_id,time_intervall,possession,value_slider[0],value_slider[1],sapc)
        graph=setup_timeline(formations,hd_mins)
        graph2=setup_pitch(avg_formation,hd_min)
        data={}
        data['avg_formation']=avg_formation
        data['formations']=formations
        data['hd_min']=hd_min
        data['hd_mins']=hd_mins
    return graph, graph2, data


@app.callback(Output('pitch-graph','figure'),
            [Input('timeline-graph','clickData')],
            [State('pitch-graph', 'figure'),
            State('memory', 'data')])
def test(clickData,figure,data):
    n=int(clickData['points'][0]['x'].split('F')[1])
    new_fig=draw_pitch()
    new_fig=add_formation(data['avg_formation'],new_fig)
    new_fig=add_formation(data['formations'][n],new_fig)
    return new_fig


if __name__ == '__main__':
    app.run_server(debug=True)