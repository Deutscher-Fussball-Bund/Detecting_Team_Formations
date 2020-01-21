import plotly.graph_objects as go
import numpy as np
import pandas as pd
from dashboard.scripts.array_operations import combine_xy
import dash_core_components as dcc



def add_formation(formation,fig):
    xy=combine_xy(formation)
    x=xy[0]
    y=xy[1]
    fig.add_trace(
            go.Scatter(
                x=x,
                y=y,
                mode='markers'
    ))
    return fig

def setup_pitch(avg_formation,hd_min):
    fig=draw_pitch()
    fig=add_formation(avg_formation,fig)
    graph2 = dcc.Graph(
        figure=fig,
        id='pitch-graph'
    )
    return graph2

def setup_timeline(formations,hd_mins):
    x_labels=[]
    for i,formation in enumerate(formations):
        x_labels.append('F'+str(i))
        
    y_labels=[]
    d=[]
    for i,hd_min in enumerate(hd_mins):
        #print(hd_min)
        #if hd_min[0] not in y_labels:
        #    y_labels.append(hd_min[0])
        d.append([x_labels[i],hd_min[0]])
        y_labels.append(hd_min[0])

    fig = go.Figure()
    # Create and style traces
    fig.add_trace(go.Scatter(x=x_labels, y=y_labels, name='Formations', mode='markers'))#, line_shape='hv', line=dict(color='grey', width=4)))

    # Edit the layout
    fig.update_layout(title='Average Formations',
                    xaxis_title='Time',
                    yaxis_title='Formation')

    graph = dcc.Graph(
        figure=fig,
        id='timeline-graph'
    )
    return graph

#Creates a Circle
def make_circle(center, radius, n_points=75):
    t=np.linspace(0, 1, n_points)
    x=center[0]+radius*np.cos(2*np.pi*t)
    y=center[1]+radius*np.sin(2*np.pi*t)
    return x, y 

def draw_pitch():
    #SVG path for Centre Circle
    x,y=make_circle([0,0], 9.15)

    path='M '+str(x[0])+','+str(y[1])
    for k in range(1, x.shape[0]):
        path+=' L '+str(x[k])+','+str(y[k])
    path+=' Z'

    fig = go.Figure()

    # Set axes ranges
    fig.update_xaxes(scaleanchor = "y")
    fig.update_xaxes(range=[-53.5, 53.5])
    fig.update_yaxes(range=[-35.5, 35.5])
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)
    fig.update_layout(plot_bgcolor='#195905', autosize=False, showlegend=False)
    fig.update_layout(margin=dict(l=35, r=35, t=30, b=20))

    # Add Halfway line
    fig.add_shape(
            go.layout.Shape(
                type="line",
                x0=0,
                y0=34,
                x1=0,
                y1=-34,
                line=dict(
                    color="White",
                    width=2
                )
    ))

    fig.update_layout(
        shapes=[
            go.layout.Shape(),
            #Side and Goal lines
            go.layout.Shape(
                type="rect",
                x0=-52.5,
                y0=-34,
                x1=52.5,
                y1=34,
                line=dict(
                    color="White",
                ),
            ),
            #Left 5m Box
            go.layout.Shape(
                type="rect",
                x0=-52.5,
                y0=-9.16,
                x1=-52.5+5.5,
                y1=9.16,
                line=dict(
                    color="White",
                ),
            ),
            #Right 5m Box
            go.layout.Shape(
                type="rect",
                x0=52.5,
                y0=9.16,
                x1=52.5-5.5,
                y1=-9.16,
                line=dict(
                    color="White",
                ),
            ),
            #Left Box
            go.layout.Shape(
                type="rect",
                x0=-52.5,
                y0=20.16,
                x1=-52.5+16.5,
                y1=-20.16,
                line=dict(
                    color="White",
                ),
            ),
            #Right Box
            go.layout.Shape(
                type="rect",
                x0=52.5,
                y0=20.16,
                x1=52.5-16.5,
                y1=-20.16,
                line=dict(
                    color="White",
                ),
            ),
            # Quadratic Bezier Curves
            go.layout.Shape(
                type="path",
                #path="M -52.5+16.5,8 C -52.5+11+9,8 -52.5+11+9,-8 -52.5+16.5,-8",
                #path="M -36,7.5 C -32.35,7.5 -32.35,-7.5 -36,-7.5", Q -32.35,0 -36,-7.5"
                path="M -36,7.5 Q -31,0 -36,-7.5",
                line_color="White",
            ),
            go.layout.Shape(
                type="path",
                path="M 36,7.5 Q 31,0 36,-7.5",
                line_color="White",
            ),
            #Centre Circle
            go.layout.Shape(
                type="path",
                path=path,
                line_color="White",
            ),
            #Centre Spot
            go.layout.Shape(
                type="circle",
                xref="x",
                yref="y",
                fillcolor="White",
                x0=-0.4,
                y0=-0.4,
                x1=0.4,
                y1=0.4,
                line_color="White",
            ),
            #Penalty Spot left
            go.layout.Shape(
                type="circle",
                xref="x",
                yref="y",
                fillcolor="White",
                x0=-52.5+11-0.4,
                y0=-0.4,
                x1=-52.5+11+0.4,
                y1=0.4,
                line_color="White",
            ),
            #Penalty Spot right
            go.layout.Shape(
                type="circle",
                xref="x",
                yref="y",
                fillcolor="White",
                x0=52.5-11-0.4,
                y0=-0.4,
                x1=52.5-11+0.4,
                y1=0.4,
                line_color="White",
            ),
        ]
    )
    
    fig.update_shapes(dict(xref='x', yref='y'))
    return fig