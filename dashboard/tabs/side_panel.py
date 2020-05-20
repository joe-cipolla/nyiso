import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
from dash.dependencies import Input, Output
from dashboard.app import app
from dashboard.tabs import tab_1, tab_2
from dashboard import test_data


df = test_data.default_df
# min_p = df['he01'].min()
# max_p = df['he16'].max()
min_p = 0
max_p = 50
layout = html.Div([
    html.H1('NYISO Dash'),
    dbc.Row([
        dbc.Col(html.Div([
            html.H2('Filters'),

            html.Div([
                html.P(),
                html.H5('ISO'),
                dcc.Dropdown(id='iso-drop',
                             options=[{'iso': i, 'value': i} for i in df.iso.unique()],
                             value=[],
                             multi=True)
            ]),

            html.Div([
                html.P(),
                html.H5('Zone'),
                dcc.Dropdown(id='zone-drop',
                             options=[{'zone': i, 'value': i} for i in df.zone.unique()],
                             value=[],
                             multi=True)
            ]),

            dcc.Checklist(id='rating-95',
                          options=[{'he01': 'Only HE01 >= $5 ', 'value': 'Y'}]),
            html.Div([
                html.P(),
                html.H5('Price Slider'),
                dcc.RangeSlider(id='price-slider',
                                min=min_p,
                                max=max_p,
                                marks={0: '$0', 10: '$10', 15: '$15', 20: '$20', 25: '$25', 30: '$30', 35: '$35'},
                                value=[0, 9999])
            ]),
        ], style={'marginBottom': 50, 'marginTop': 25, 'marginLeft': 15, 'marginRight': 15}), width=3),
        dbc.Col(html.Div([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                dcc.Tab(label='Data Table', value='tab-1'),
                dcc.Tab(label='Scatter Plot', value='tab-2'),
                dcc.Tab(label='Heatmap Plot', value='tab-3'),
            ]),
            html.Div(id='tabs-content')
        ]), width=9)
    ])
])


@app.callback(Output('zone-drop', 'options'),
              [Input('zone-drop', 'value')])
def set_zone_options(zones):
    if len(zones) > 0:
        return [{'label': i, 'value': i} for i in sorted(set(df['zone'].loc[df['iso'].isin(zones)]))]
    else:
        return df.zone.unique().tolist()


@app.callback(Output('iso-drop', 'options'),
              [Input('zone-drop', 'value')])
def set_iso_options(isos):
    if len(isos) > 0:
        return [{'label': i, 'value': i} for i in sorted(set(df['zone'].loc[df['iso'].isin(isos)]))]
    else:
        return df.iso.unique().tolist()
