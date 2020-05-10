""" loads csv/txt data files from disk into PostgreSQL database"""

import nyiso_sql.sql_utils as qutil
import nyiso_sql.global_vars as gvars
import pandas as pd


def load_data(start_date, end_date, data_types, root_path=gvars.root_dir):
    """
    :param start_date - date string (YYYY-MM-DD)
    :param end_date - date string (YYYY-MM-DD)
    :param data_types - list of strings
    :param root_path - string
    """
    for data_type in data_types:
        for file_date in pd.date_range(start_date, end_date, freq='D'):
            file_path = root_path + data_type + '/' \
                        + str(file_date.year) \
                        + '{:02d}'.format(file_date.month) \
                        + '{:02d}'.format(file_date.day) \
                        + data_type + gvars.url_file_name_map[data_type][4] \
                        + '.' + gvars.url_file_name_map[data_type][2]
            records = pd.read_csv(file_path)
            records = reformat_damlbmp(records)
            
            qutil.bulk_insert_rows(
                gvars.url_file_name_map[data_type][5],
                records
            )


def reformat_damlbmp(df):

    df = df[['Time Stamp', 'Name', 'LBMP ($/MWHr)']]
    df = df.pivot(index='Name', columns='Time Stamp', values='LBMP ($/MWHr)')
    df.index.name = None

    df_date = pd.to_datetime(df.columns[0]).strftime('%Y-%m-%d')
    # date_id = qutil.lookup_value_in_table('date_id', df_date)
    date_id = 1

    records = []
    for i in range(df.__len__()):
        print(i)
        i_record = df.iloc[0, :].values.tolist()
        zone_name = df.index[i]
        print(zone_name)
        zone_id = qutil.lookup_value_in_table('zone_id_with_iso_zone_name', zone_name)
        i_record.insert(0, zone_id)
        i_record.insert(0, date_id)
        records.append(tuple(i_record))

    return records


if __name__ == '__main__':
    df = pd.read_csv('/Users/joecipolla/Dropbox/Reference/Project_Seldon/Data/NYISO/damlbmp/20200401damlbmp_zone.csv')
    print(df)
    df = reformat_damlbmp(df)
    print(df)
