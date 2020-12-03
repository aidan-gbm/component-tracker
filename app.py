import os
import dash
import datetime
import pandas as pd
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from tracker import Tracker

cTracker = Tracker()
app = dash.Dash(__name__)

colors = {
    'background': '#b0ceff',
    'text': '#040a14'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='PC Component Tracker',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(id='last-updated', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(id='live-graph'),
    dcc.Interval(
        id='interval-component',
        interval=30*1000,
        n_intervals=0
    )
])

@app.callback(
    Output('last-updated', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_time(n):
    date = datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')
    return html.P('Last updated: ' + date)

@app.callback(
    Output('live-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    cTracker.update()

    data = {}
    for f in os.listdir('./data'):
        name = f.split('.')[0].replace('_', ' ')
        data[name] = pd.read_csv('./data/' + f)

    lines = []
    for name, dataset in data.items():
        lines.append(go.Scatter(name=name, x=dataset['date'], y=dataset['price'], line_shape='linear'))
    fig = go.Figure(lines)
    fig.update_layout(
        xaxis_title='Timestamp',
        yaxis_title='Price',
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],
        legend=dict(
            font_size=16,
            orientation='h',
            yanchor='bottom',
            y=-0.5,
            xanchor='left',
            x=0
        )
    )
    return fig

app.run_server(debug=False)