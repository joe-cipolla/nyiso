import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_table
from dashboard.app import app
from dashboard import test_data
from dashboard.tabs import side_panel


df = test_data.default_df

layout = html.Div(
    id='table-paging-with-graph-container',
    className="five columns"
)


@ app.callback(
    Output('table-paging-with-graph-container', "children"),
    [Input('rating-95', 'value'), side_panel.Input('price-slider', 'value')]
)
def update_graph(ratingcheck, prices):
    dff = df
    low = prices[0]
    high = prices[1]

    dff = dff.loc[(dff['he01'] >= low) & (dff['he01'] <= high)]

    if ratingcheck == ['Y']:
        dff = dff.loc[dff['he02'] >= 10]

    trace1 = go.Scattergl(
        x=dff['he02'],
        y=dff['he01'],
        mode='markers',
        opacity=0.7,
        marker={
            'size': 8, 'line': {'width': 0.5, 'color': 'white'}
        },
        name='HE01 v HE02'
    )
    return html.Div([
        dcc.Graph(
            id='rating-price',
            figure={
                'data': [trace1],
                'layout': dict(
                    xaxis={'type': 'log', 'title': 'he02'},
                    yaxis={'title': 'he01'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        )
    ])
