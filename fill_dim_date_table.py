import pandas as pd
import nyiso_sql.sql_utils as qutil


date_range = pd.date_range('1999-01-01', '2034-12-31')

records = []
for t_date in date_range:
    date = t_date.strftime('%Y-%m-%d')
    weekday_id = qutil.lookup_value_in_table('weekday_id', t_date.strftime('%a').upper())
    month_id = qutil.lookup_value_in_table('month_id', t_date.strftime('%b').upper())
    year_id = qutil.lookup_value_in_table('year_id', str(t_date.year))
    season_id = qutil.lookup_value_in_table('season_id', t_date.strftime('%b').upper())
    quarter_id = qutil.lookup_value_in_table('quarter_id', t_date.strftime('%b').upper())
    records.append((date, weekday_id, month_id, year_id, season_id, quarter_id))
    print(date)

qutil.bulk_insert_rows('dim_date', records)
