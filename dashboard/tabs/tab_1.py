import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
from dash.dependencies import Input, Output
from dashboard.app import app
from dashboard import test_data


df = test_data.default_df
PAGE_SIZE = 50

layout = html.Div(
    dash_table.DataTable(
        id='table-sorting-filtering',
        columns=[
            {'name': i, 'id': i, 'deletable': True} for i in
            df[['date', 'iso', 'zone', 'he01', 'he02', 'he03', 'he04', 'he05', 'he06', 'he07',
                'he08', 'he09', 'he10', 'he11', 'he12', 'he13', 'he14', 'he15', 'he16',
                'he17', 'he18', 'he19', 'he20', 'he21', 'he22', 'he23', 'he24']]
        ],
        style_table={'height': '750px', 'overflowX': 'scroll'}, style_data_conditional=[
            {'if': {'row_index': 'odd'},
             'backgroundColor': 'rgb(248, 248, 248)'}
        ],
        style_cell={
            'height': '90',
            # all three widths are needed
            'minWidth': '140px', 'width': '140px', 'maxWidth': '140px', 'textAlign': 'left', 'whiteSpace': 'normal'
        },
        style_cell_conditional=[
            {'if': {'column_id': 'date'}, 'width': '48%'},
            {'if': {'column_id': 'zone'}, 'width': '18%'},
        ],
        page_current=0,
        page_size=PAGE_SIZE,
        page_action='custom',
        filter_action='custom',
        filter_query='',
        sort_action='custom',
        sort_mode='multi',
        sort_by=[]
    )
)
