import io
import base64
import os.path
import math

import dash
import dash_resumable_upload
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from dashboard.tab_one import create_tab_one,add_match_controls,add_match_settings
from dashboard.tab_two import create_tab_two,create_second_upload,create_right_column
from dashboard.file_management import new_match,move_match,delete_selected_rows
from dashboard.pitch import draw_pitch

from dashboard.scripts.start_analysis import start_analysis

import plotly.graph_objects as go


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

dash_resumable_upload.decorate_server(app.server, "./uploads")

app.layout = html.Div([
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
    print(tab)
    if tab == 'tab-1':
        return create_tab_one()
    elif tab == 'tab-2':
        return create_tab_two()
    

@app.callback(Output('another-column', 'children'),
                [Input('upload_matchinfo', 'contents')],
                [State('upload_matchinfo', 'filename')])
                #[Input('upload_matchinfo', 'fileNames')])
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


@app.callback(Output('ex_secs','children'),
               [Input('knob','value')])
def make(value):
    return 'Exclude Seconds After Possession Change: {:0.2f}'.format(math.ceil(value*4)/4)


@app.callback(Output('gr', 'children'),
                [Input('start-btn', 'n_clicks')],
                [State('match-select','value'),
                State('team-select', 'value'),
                State('slider-window', 'value'),
                State('time-input', 'value'),
                State('possession-radio', 'value'),
                State('knob','value')]
)
def check_values(n_clicks,match_id,team_id,value_slider,time_intervall,possession,sapc):
    if n_clicks is not None:
        dirname=os.path.dirname(__file__)
        uploads_path=os.path.join(dirname, '../uploads/'+match_id)
        path=uploads_path+'/positions_raw_'+match_id+'.xml'
        info_path=uploads_path+'/matchinformation_'+match_id+'.xml'
        print(match_id)
        print(team_id)
        print(value_slider) #Immer richtig
        print(time_intervall)
        print(possession)
        print(sapc)
        #start_analysis(path,info_path,match_id,team_id,time_intervall,possession,value_slider[0],value_slider[1],sapc)
    return show_dummy()

def show_dummy():

    import plotly.figure_factory as ff

    df = [dict(Start='2020-08-01 00:00:00', Finish='2020-08-01 00:02:30', Resource='5-2-3', Task=''),
        dict(Start='2020-08-01 00:02:30', Finish='2020-08-01 00:05:50', Resource='3-4-3', Task=''),
        dict(Start='2020-08-01 00:08:30', Finish='2020-08-01 00:12:20', Resource='4-3-3', Task=''),
        dict(Start='2020-08-01 00:12:20', Finish='2020-08-01 00:22:00', Resource='5-2-3', Task=''),
        dict(Start='2020-08-01 00:32:00', Finish='2020-08-01 00:43:20', Resource='4-3-3', Task=''),
        dict(Start='2020-08-01 00:54:00', Finish='2020-08-01 01:04:20', Resource='4-3-3', Task=''),
        dict(Start='2020-08-01 01:05:18', Finish='2020-08-01 01:06:18', Resource='4-3-3', Task=''),
        dict(Start='2020-08-01 01:11:14', Finish='2020-08-01 01:23:14', Resource='5-2-3', Task='')]

    colors = {'4-3-3': 'rgb(220, 0, 0)',
            '3-4-3': 'rgb(20, 0, 220)',
            '5-2-3': 'rgb(0, 255, 100)'}


    

    fig=draw_pitch()
    fig.add_trace(
            go.Scatter(
                x=[-30+11, 30-11],
                y=[0, 0],
                mode='markers'
    ))
    
    fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True,
                        group_tasks=True)
    return dcc.Graph(
        figure=fig,
        id='my-graph'
    )  

if __name__ == '__main__':
    app.run_server(debug=True)