import chart_studio.plotly as py
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


# basic plotly scatter plot
trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 54, 11, 9]
)
data = [trace0, trace1]
py.plot(data, filename='basic-line', auto_open=True)


# pandas plotting
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

fig = go.Figure(go.Scatter(x=df.gdpPercap, y=df.lifeExp, text=df.country, mode='markers', name='2007'))
fig.update_xaxes(title_text='GDP per Capita', type='log')
fig.update_yaxes(title_text='Life Expectancy')
fig.update_layout(title='Gapminder 2007', showlegend=True)
py.plot(fig, filename='pandas-multiple-scatter')


# dash plot
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])
app.run_server(debug=True, use_reloader=False)  # turn off reloader if inside Jupyter
