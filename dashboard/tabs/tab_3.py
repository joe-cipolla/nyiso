import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from dashboard.app import app
from dashboard import test_data


df = test_data.default_df

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
    [Input("iso-drop", "value")
        , Input("zone-drop", "value")
        , Input("selected-feature", "value")
        , Input("date-drop", 'value')
     ])
def update_figure(iso, date, zone):
    dff = test_data.default_df
    dff = dff.groupby(['zone', 'date']).mean().reset_index()
    dff = dff.loc[dff['zone'].isin(zone)]

    if zone is None:
        zone = []

    if len(iso) > 0 and len(zone) > 0 and len(date) > 0:
        dff = dff.loc[dff['zone'].isin(zone) & dff['zone'].isin(zone) & dff['date'].isin(date)]

    elif len(iso) > 0 and len(zone) > 0 and len(date) == 0:
        dff = dff.loc[dff['zone'].isin(zone) & dff['zone'].isin(zone)]

    elif len(iso) > 0 and len(zone) == 0 and len(date) > 0:
        dff = dff.loc[dff['zone'].isin(zone) & dff['date'].isin(date)]

    elif len(iso) > 0 and len(zone) == 0 and len(date) == 0:
        dff = dff.loc[dff['zone'].isin(zone)]

    trace = go.Heatmap(z=dff[zone]
                       , x=dff['iso']
                       , y=dff['date']
                       , hoverongaps=True
                       , colorscale='rdylgn', colorbar={"title": "Average", 'x': -.09}, showscale=True)
    return {"data": [trace], "layout": {
        "xaxis": {"automargin": False},
        "yaxis": {"automargin": True, 'side': "right"},
        "margin": {"t": 10, "l": 30, "r": 100, "b": 230}
    }}
