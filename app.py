import io
import base64
import os.path

import dash
import dash_resumable_upload
import dash_html_components as html
from dash.dependencies import Input, Output

from tacticon.RawEventDataReader import RawEventDataReader
import xml.etree.ElementTree as ET

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

dash_resumable_upload.decorate_server(app.server, "uploads")

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

    html.Div(id='output'),

    html.Img(id='pitch')
])


@app.callback(Output('pitch', 'src'),
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