import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from dashboard.app import app
from dashboard.database import transforms


df = pd.read_csv('data/default_df.csv')

layout = html.Div([
    html.Div([html.H3("Visualize:")], style={'textAlign': "Left"}),
    html.Div([dcc.Dropdown(id="selected-feature", options=[{"label": i, "value": i} for i in ['he07', 'he08']],
                           value='price', style={"display": "block", "width": "80%"})
              ]),
    html.Div([dcc.Graph(id="ru-my-heatmap",
                        style={"margin-right": "auto", "margin-left": "auto", "width": "80%", "height": "700px"})]
             )
])


@app.callback(
    Output("ru-my-heatmap", "figure"),
    [Input("country-drop", "value")
        , Input("province-drop", "value")
        , Input("selected-feature", "value")
        , Input("variety-drop", 'value')

     ])
def update_figure(zone, date, province):
    dff = transforms.df
    dff = dff.groupby(['zone', 'date']).mean().reset_index()
    dff = dff.loc[dff['zone'].isin(zone)]

    if province is None:
        province = []

    if len(zone) > 0 and len(province) > 0 and len(date) > 0:
        dff = dff.loc[dff['zone'].isin(zone) & dff['province'].isin(province) & dff['date'].isin(date)]

    elif len(zone) > 0 and len(province) > 0 and len(date) == 0:
        dff = dff.loc[dff['zone'].isin(zone) & dff['province'].isin(province)]

    elif len(zone) > 0 and len(province) == 0 and len(date) > 0:
        dff = dff.loc[dff['zone'].isin(zone) & dff['date'].isin(date)]

    elif len(zone) > 0 and len(province) == 0 and len(date) == 0:
        dff = dff.loc[dff['zone'].isin(zone)]

    trace = go.Heatmap(z=dff[province]
                       , x=dff['zone']
                       , y=dff['date']
                       , hoverongaps=True
                       , colorscale='rdylgn', colorbar={"title": "Average", 'x': -.09}, showscale=True)
    return {"data": [trace], "layout": {
        "xaxis": {"automargin": False},
        "yaxis": {"automargin": True, 'side': "right"},
        "margin": {"t": 10, "l": 30, "r": 100, "b": 230}
    }}
