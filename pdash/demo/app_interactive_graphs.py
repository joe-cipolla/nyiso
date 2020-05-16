import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

np.random.seed(0)
df2 = pd.DataFrame({"Col " + str(i+1): np.random.rand(30) for i in range(6)})

available_indicators = df['Indicator Name'].unique()

app.layout = html.Div([
    html.Div([
        # update on hover
        dcc.Markdown('''## Update Graph on Hover'''),
    ], style={'backgroundColor': 'rgb(250, 250, 250)', 'padding': '10px 5px'}),

    html.Div([
        html.Div([

            html.Div([
                dcc.Dropdown(
                    id='crossfilter-xaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value='Fertility rate, total (births per woman)'
                ),
                dcc.RadioItems(
                    id='crossfilter-xaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                    value='Linear',
                    labelStyle={'display': 'inline-block'}
                )
            ], style={'width': '49%', 'display': 'inline-block'}),

            html.Div([
                dcc.Dropdown(
                    id='crossfilter-yaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value='Life expectancy at birth, total (years)'
                ),
                dcc.RadioItems(
                    id='crossfilter-yaxis-type',
                    options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                    value='Linear',
                    labelStyle={'display': 'inline-block'}
                )
            ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
        ], style={
            'borderBottom': 'thin lightgrey solid',
            'backgroundColor': 'rgb(250, 250, 250)',
            'padding': '10px 5px'
        }),

        html.Div([
            dcc.Graph(
                id='crossfilter-indicator-scatter',
                hoverData={'points': [{'customdata': 'Japan'}]}
            )
        ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20 '}),

        html.Div([
            dcc.Graph(id='x-time-series'),
            dcc.Graph(id='y-time-series'),
        ], style={'display': 'inline-block', 'width': '49%'}),

        html.Div(dcc.Slider(
            id='crossfilter-year--slider',
            min=df['Year'].min(),
            max=df['Year'].max(),
            value=df['Year'].max(),
            marks={str(year): str(year) for year in df['Year'].unique()},
            step=None
        ), style={'width': '49%', 'padding': '0px 20px 20px 20px'}),
    ]),

    dcc.Markdown('''&nbsp;\n'''),
    dcc.Markdown('''&nbsp;\n'''),
    dcc.Markdown('''---'''),

    # Generic Crossfilter Recipe
    dcc.Markdown('''## Generic Crossfilter Recipe'''),

    html.Div([
        html.Div(
            dcc.Graph(id='g1', config={'displayModeBar': False}),
            className='four columns'
        ),
        html.Div(
            dcc.Graph(id='g2', config={'displayModeBar': False}),
            className='four columns'
        ),
        html.Div(
            dcc.Graph(id='g3', config={'displayModeBar': False}),
            className='four columns'
        )
    ], className='row'),
])


@app.callback(
    dash.dependencies.Output('crossfilter-indicator-scatter', 'figure'),
    [dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-xaxis-type', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-type', 'value'),
     dash.dependencies.Input('crossfilter-year--slider', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    dff = df[df['Year'] == year_value]

    return {
        'data': [dict(
            x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
            y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
            text=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
            customdata=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': dict(
            xaxis={
                'title': xaxis_column_name,
                'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_column_name,
                'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 30, 't': 10, 'r': 0},
            height=450,
            hovermode='closest'
        )
    }


def create_time_series(dff, axis_type, title):
    return {
        'data': [dict(
            x=dff['Year'],
            y=dff['Value'],
            mode='lines+markers'
        )],
        'layout': {
            'height': 225,
            'margin': {'l': 20, 'b': 30, 'r': 10, 't': 10},
            'annotations': [{
                'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                'text': title
            }],
            'yaxis': {'type': 'linear' if axis_type == 'Linear' else 'log'},
            'xaxis': {'showgrid': False}
        }
    }


@app.callback(
    Output('x-time-series', 'figure'),
    [Input('crossfilter-indicator-scatter', 'hoverData'),
     Input('crossfilter-xaxis-column', 'value'),
     Input('crossfilter-xaxis-type', 'value')])
def update_y_timeseries(hoverData, xaxis_column_name, axis_type):
    country_name = hoverData['points'][0]['customdata']
    dff = df[df['Country Name'] == country_name]
    dff = dff[dff['Indicator Name'] == xaxis_column_name]
    title = '<b>{}</b><br>{}'.format(country_name, xaxis_column_name)
    return create_time_series(dff, axis_type, title)


@app.callback(
    Output('y-time-series', 'figure'),
    [Input('crossfilter-indicator-scatter', 'hoverData'),
     Input('crossfilter-yaxis-column', 'value'),
     Input('crossfilter-yaxis-type', 'value')])
def update_x_timeseries(hoverData, yaxis_column_name, axis_type):
    dff = df[df['Country Name'] == hoverData['points'][0]['customdata']]
    dff = dff[dff['Indicator Name'] == yaxis_column_name]
    return create_time_series(dff, axis_type, yaxis_column_name)


def get_figure(df, x_col, y_col, selected_points, selectedpoints_local):

    if selectedpoints_local and selectedpoints_local['range']:
        ranges = selectedpoints_local['range']
        selection_bounds = {'x0': ranges['x'][0], 'x1': ranges['x'][1],
                            'y0': ranges['y'][0], 'y1': ranges['y'][1]}
    else:
        selection_bounds = {'x0': np.min(df2[x_col]), 'x1': np.max(df2[x_col]),
                            'y0': np.min(df2[y_col]), 'y1': np.max(df2[y_col])}

    # set which points are selected with the 'selectedpoints' property
    # and style those points with the 'selected' and 'unselected' attributed.
    # https://medium.com/@plotlygraphs/notes-from-the-latest-plotly-js-release-b035a5b43
    return{
        'data': [{
            'x': df2[x_col],
            'y': df2[y_col],
            'text': df2.index,
            'textposition': 'top',
            'selectedpoints': selected_points,
            'customdata': df2.index,
            'type': 'scatter',
            'mode': 'markers+text',
            'marker': {'color': 'rgba(0, 116, 217, 0.7)', 'size': 12},
            'unselected': {
                'marker': {'opacity': 0.3},
                # make text transparent when not selected
                'textfont': {'color': 'rgba(0, 0, 0, 0)'}
            }
        }],
        'layout': {
            'margin': {'1': 20, 'r': 0, 'b': 15, 't': 5},
            'dragmode': 'select',
            'hovermode': False,
            # display a rectangle to highlight the previously selected region
            'shapes': [dict({
                'type': 'rect',
                'line': {'width': 1, 'dash': 'dot', 'color': 'darkgrey'}
            }, **selection_bounds
            )]
        }
    }


# this callback defines 3 figures
# as a function of the intersection of their 3 selections
@app.callback(
    [Output('g1', 'figure'),
     Output('g2', 'figure'),
     Output('g3', 'figure')],
    [Input('g1', 'selectedData'),
     Input('g2', 'selectedData'),
     Input('g3', 'selectedData')]
)
def callback(selection1, selection2, selection3):
    selected_points = df2.index
    for selected_data in [selection1, selection2, selection3]:
        if selected_data and selected_data['points']:
            selected_points = np.intersect1d(selected_points,
                                            [p['customdata'] for p in selected_data['points']])

    return [get_figure(df2, 'Col 1', 'Col 2', selected_points, selection1),
            get_figure(df2, 'Col 3', 'Col 4', selected_points, selection2),
            get_figure(df2, 'Col 5', 'Col 6', selected_points, selection3)]


if __name__ == '__main__':
    app.run_server(debug=True)
