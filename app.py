import base64
import datetime
import io

import dash
import dash_resumable_upload
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import pandas as pd

from formations import say_hi
import xml.etree.ElementTree as ET

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

dash_resumable_upload.decorate_server(app.server, "uploads")

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
   dcc.Upload(
        id='upload-data',
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
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),

])

@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'filename')],
              [State('upload-data', 'contents'),
               State('upload-data', 'last_modified')])
def update_output(filename, contents, last_modified):
    print(filename)
    if filename is not None:
        print(filename)
        for c in contents:
            decode = base64.b64decode(c.split(',')[1]).decode('utf8')
            #print(decode)
            root_matchinformation=ET.fromstring(decode)
            
        for player in root_matchinformation.iter('FrameSet'):
                print(player.get('PlayerId'))
    return html.Ul(html.Li("No Files Uploaded Yet!"))

#@app.callback(Output('output-data-upload', 'children'),
#              [Input('upload-data', 'contents')],
#              [State('upload-data', 'filename'),
#               State('upload-data', 'last_modified')])
#def update_output(contents, filename, last_modified):
#    #print(contents)
#    print(filename)
#    print(last_modified)
#    for c in contents:
#        decode = base64.b64decode(c.split(',')[1]).decode('utf8')
#        print(decode)
#        #matchinformation = ET.fromstring(decode)
#        #root_matchinformation = matchinformation.getroot()
#        root_matchinformation=ET.fromstring(decode)
#        
#       for player in root_matchinformation.iter('FrameSet'):
#            print(player.get('PlayerId'))




    #if list_of_contents is not None:
     #   children = [
      #      parse_contents(c, n, d) for c, n, d in
       #     zip(list_of_contents, list_of_names, list_of_dates)]
        #return children

#def parse_contents(contents, filename, sessionId):
#    decoded = base64.b64decode(content_string)
#    stringToXML = ET.ElementTree(ET.fromstring(decoded))
#    root = tree.getroot()
#    for a in root:

if __name__ == '__main__':
    app.run_server(debug=True)