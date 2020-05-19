import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import sqlite3
import pandas as pd
from dashboard.app import app
from dashboard.tabs import side_panel, tab_1, tab_2, tab_3, navbar
from dashboard import test_data


app.layout = html.Div([navbar.Navbar()
                          , side_panel.layout
                       ])


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return tab_1.layout
    elif tab == 'tab-2':
        return tab_2.layout
    elif tab == 'tab-3':
        return tab_3.layout


operators = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]


def split_filter_part(filter_part):
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]
                value_part = value_part.strip()
                v0 = value_part[0]
                if v0 == value_part[-1] and v0 in ("'", '"', '`'):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part
                # word operators need spaces after them in the filter string,
                # but we don't want these later
                return name, operator_type[0].strip(), value
    return [None] * 3


@app.callback(
    Output('table-sorting-filtering', 'data')
    , [Input('table-sorting-filtering', "page_current")
        , Input('table-sorting-filtering', "page_size")
        , Input('table-sorting-filtering', 'sort_by')
        , Input('table-sorting-filtering', 'filter_query')
        , Input('rating-95', 'value')
        , Input('price-slider', 'value')
        , Input('iso-drop', 'value')
        , Input('zone-drop', 'value')
        , Input('date-drop', 'value')
       ])
def update_table(page_current, page_size, sort_by, filter, ratingcheck, prices, iso, zone, date):
    filtering_expressions = filter.split(' && ')
    dff = test_data.default_df


    low = prices[0]
    high = prices[1]
    dff = dff.loc[(dff['HE01'] >= low) & (dff['HE18'] <= high)]
    if zone is None:
        zone = []
    if date is None:
        date = []

    if len(iso) > 0 and len(zone) > 0 and len(date) > 0:
        dff = dff.loc[dff['iso'].isin(iso) & dff['zone'].isin(zone) & dff['date'].isin(date)]
    elif len(iso) > 0 and len(zone) > 0 and len(date) == 0:
        dff = dff.loc[dff['iso'].isin(iso) & dff['zone'].isin(zone)]
    elif len(iso) > 0 and len(zone) == 0 and len(date) > 0:
        dff = dff.loc[dff['iso'].isin(iso) & dff['date'].isin(date)]
    elif len(iso) > 0 and len(zone) == 0 and len(date) == 0:
        dff = dff.loc[dff['iso'].isin(iso)]
    else:
        dff
    if ratingcheck == ['Y']:
        dff = dff.loc[dff['HE05'] >= 5]
    else:
        dff
    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)
    if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
        # these operators match pandas series operator method names
        dff = dff.loc[getattr(dff[col_name], operator)(filter_value)]
    elif operator == 'contains':
        dff = dff.loc[dff[col_name].str.contains(filter_value)]
    elif operator == 'datestartswith':
        # this is a simplification of the front-end filtering logic,
        # only works with complete fields in standard format
        dff = dff.loc[dff[col_name].str.startswith(filter_value)]
    if len(sort_by):
        dff = dff.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )
    page = page_current
    size = page_size
    return dff.iloc[page * size: (page + 1) * size].to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)
