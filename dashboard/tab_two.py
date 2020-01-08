import dash
import dash_resumable_upload
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

def create_tab_two():
    return html.Div([
            html.Div(
                id="left-column",
                className="four columns",
                children=[dash_resumable_upload.Upload(
                    id='upload',
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
                )],
            ),
            html.Div(
                id="another-column"
            )
        ])