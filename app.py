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
                [State('team-select', 'value'),
                State('slider-window', 'value'),
                State('time-input', 'value'),
                State('possession-radio', 'value'),
                State('knob','value')]
)
def check_values(n_clicks,value_team,value_slider,value_frame,value_possession,value_knob):
    if n_clicks is not None:
        print(n_clicks) #Braucht man nicht
        print(value_team)
        print(value_slider) #Immer richtig
        print(value_frame)
        print(value_possession)
        print(value_knob)
    return show_dummy()

def show_dummy():
    return dcc.Graph(
        figure=dict(
            data=[
                dict(
                    x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                    2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                    y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                    350, 430, 474, 526, 488, 537, 500, 439],
                    name='Rest of world',
                    marker=dict(
                        color='rgb(55, 83, 109)'
                    )
                ),
                dict(
                    x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                    2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                    y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                    299, 340, 403, 549, 499],
                    name='China',
                    marker=dict(
                        color='rgb(26, 118, 255)'
                    )
                )
            ],
            layout=dict(
                title='US Export of Plastic Scrap',
                showlegend=True,
                legend=dict(
                    x=0,
                    y=1.0
                ),
                margin=dict(l=40, r=0, t=40, b=30)
            )
        ),
        style={'height': 300},
        id='my-graph'
    )  

if __name__ == '__main__':
    app.run_server(debug=True)