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


df = pd.read_csv('data/default_df.csv')
min_p = df.date.min()
max_p = df.date.max()
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
                                             500: '$500',
                                             1000: '$1000',
                                             1500: '$1500',
                                             2000: '$2000',
                                             2500: '$2500',
                                             3000: '$3000'},
                                      value=[0, 3300])
                      ]),
            html.Div([html.P(),
                      html.H5('Zone'),
                      dcc.Dropdown(id='zone-drop',
                                   options=[{'zone': i, 'value': i} for i in df.zone.unique()],
                                   value=['US'],
                                   multi=True)
                      ]),
            html.Div([html.P(),
                      html.H5('Date'),
                      dcc.Dropdown(id='date-drop',
                                   value=[],
                                   multi=True)
                      ])
            , html.Div([html.P()
                           , html.H5('HE')
                           , dcc.Dropdown(id='variety-drop',
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


@app.callback(Output('province-drop', 'options'),
              [Input('country-drop', 'value')])
def set_province_options(country):
    if len(country) > 0:
        countries = country
        return [{'label': i, 'value': i} for i in sorted(set(df['province'].loc[df['country'].isin(countries)]))]
    else:
        countries = []
        return [{'label': i, 'value': i} for i in sorted(set(df['province'].loc[df['country'].isin(countries)]))]


@app.callback(Output('variety-drop', 'options'),
              [Input('province-drop', 'value')])
def set_variety_options(province):
    if len(province) > 0:
        provinces = province
        return [{'label': i, 'value': i} for i in sorted(set(df['variety'].loc[df['province'].isin(provinces)]))]
    else:
        provinces = []
        return [{'label': i, 'value': i} for i in sorted(set(df['variety'].loc[df['province'].isin(provinces)]))]
