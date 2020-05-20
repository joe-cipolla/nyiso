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
    dbc.Row([dbc.Col(
        html.Div([
            html.H2('Filters'),
            dcc.Checklist(id='rating-95',
                          options=[{'he01': 'Only HE01 >= $5 ', 'value': 'Y'}]),
            html.Div([html.P(),
                      html.H5('Price Slider'),
                      dcc.RangeSlider(id='price-slider',
                                      min=min_p,
                                      max=max_p,
                                      marks={0: '$0',
                                             10: '$10',
                                             15: '$15',
                                             20: '$20',
                                             25: '$25',
                                             30: '$30',
                                             35: '$35'},
                                      value=[0, 9999])
                      ]),
            html.Div([html.P(),
                      html.H5('Zone'),
                      dcc.Dropdown(id='zone-drop',
                                   options=[{'zone': i, 'value': i} for i in df.zone.unique()],
                                   value=['CAPITL'],
                                   multi=True)
                      ]),
            html.Div([html.P(),
                      html.H5('Date'),
                      dcc.Dropdown(id='date-drop',
                                   value=[],
                                   multi=True)
                      ])
            , html.Div([html.P()
                           , html.H5('ISO')
                           , dcc.Dropdown(id='iso-drop',
                                          value=[],
                                          multi=True)
                        ])],
            style={'marginBottom': 50, 'marginTop': 25, 'marginLeft': 15, 'marginRight': 15}),
        width=3),
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
def set_zone_options(iso):
    if len(iso) > 0:
        countries = iso
        return [{'label': i, 'value': i} for i in sorted(set(df['zone'].loc[df['iso'].isin(countries)]))]
    else:
        countries = []
        return [{'label': i, 'value': i} for i in sorted(set(df['zone'].loc[df['iso'].isin(countries)]))]


@app.callback(Output('date-drop', 'options'),
              [Input('zone-drop', 'value')])
def set_date_options(zone):
    if len(zone) > 0:
        zones = zone
        return [{'label': i, 'value': i} for i in sorted(set(df['date'].loc[df['zone'].isin(zones)]))]
    else:
        zones = []
        return [{'label': i, 'value': i} for i in sorted(set(df['date'].loc[df['zone'].isin(zones)]))]
