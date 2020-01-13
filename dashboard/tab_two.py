import pandas as pd

import dash
import dash_resumable_upload
import dash_core_components as dcc
import dash_html_components as html
import dash_table

from dash.dependencies import Input, Output

from dashboard.file_management import create_match_table

def create_tab_two():
    left_column=create_left_column()
    right_column=create_right_column()
    return html.Div([
            left_column,
            right_column    
        ])

def create_left_column():
    return html.Div(
            id="left-column",
            className="four columns",
            children=[
                html.H5(
                    'Please upload a matchinformation.xml first.',
                    style={'textAlign': 'center'}
                ),
                dcc.Upload(
                    id='upload_matchinfo',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files')
                    ]),
                    style={
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
                
                html.Div(
                    id="another-column",
                    children=[]
                )],
            )

def create_right_column():
    df=create_match_table()
    return html.Div(
            id="right-column",
            className="eight columns",
            children=[
                dash_table.DataTable(
                    id='datatable',
                    data=df.to_dict('records'),
                    columns=[{'id': c, 'name': c, 'hideable':True} for c in df.columns],

                    sort_action='native',
                    sort_mode='multi',

                    style_as_list_view=True,
                    style_cell={
                        'padding': '5px',
                        'overflow': 'hidden',
                        'textOverflow': 'ellipsis',
                        'maxWidth': 0,
                        'width': 'auto'
                    },
                    style_header={
                        'backgroundColor': 'white',
                        'fontWeight': 'bold'
                    },
                    style_cell_conditional=[
                        {
                            'if': {'column_id': c},
                            'textAlign': 'left'
                        } for c in ['HomeTeam', 'GuestTeam']
                    ]
                ) 
            ]
        )

def create_second_upload(match_title):
    return html.Div([
            html.H5(
                'Next, please upload the position data for the game',
                style={'textAlign': 'center'}
            ),
            html.H6(
                match_title.replace(":", " - "),
                style={'textAlign': 'center'}
            ),
            dash_resumable_upload.Upload(
            id='upload_position',
            maxFiles=1,
            maxFileSize=1024*1024*1000,  # 100 MB
            service="/upload_resumable",
            textLabel="Drag and Drop here to upload!",
            startButton=False,
            pauseButton=False,
            cancelButton=False,
            defaultStyle={
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px'
            },
            activeStyle={
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'solid',
                'borderRadius': '5px'
            },
            # Allow multiple files to be uploaded
            #multiple=True
        ),
        html.Div(
            id="yet-another-column",
            children=[]
        )]
    )