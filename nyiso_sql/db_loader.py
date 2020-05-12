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

    if not isinstance(data_types, list):
        raise ValueError('data_types must be a list')

    for data_type in data_types:

        table_name = gvars.url_file_name_map[data_type][5]
        for file_date in pd.date_range(start_date, end_date, freq='D'):
            file_path = root_path + data_type + '/' \
                        + str(file_date.year) \
                        + '{:02d}'.format(file_date.month) \
                        + '{:02d}'.format(file_date.day) \
                        + data_type + gvars.url_file_name_map[data_type][4] \
                        + '.' + gvars.url_file_name_map[data_type][2]
            records = pd.read_csv(file_path)
            records = reformat_damlbmp(records, data_type)

            qutil.bulk_insert_rows(
                table_name,
                records,
                print_msg=False
            )
            print(file_date.strftime('%Y-%m-%d') + ' ' + str(data_type) + ' inserted into database')


def reformat_damlbmp(df, data_type):

    column_subset = gvars.url_file_column_map[data_type]
    time_stamp = column_subset[0]

    df_date = pd.to_datetime(df[time_stamp][0]).strftime('%Y-%m-%d')
    date_id = qutil.lookup_value_in_table('date_id', df_date)
    is_dst = qutil.check_if_dst(df_date)

    if is_dst == (0, 1):  # date is dst end_date (has extra HE02)
        df['time_name'] = df[time_stamp] + '_' + df[column_subset[1]]
        df = df.drop_duplicates('time_name')

    if qutil.check_if_date_in_table(str(date_id), data_type):
        raise ValueError(df_date + ' already present in ' + gvars.url_file_name_map[data_type][5])

    df = df[column_subset]
    df = df.pivot(index=column_subset[1], columns=time_stamp, values=column_subset[2])
    df.index.name = None

    records = []
    for i in range(df.__len__()):
        i_record = df.iloc[i, :].values.tolist()
        if is_dst == (1, 0):  # is dst start_date (has missing HE03)
            i_record.insert(2, i_record[1])

        if data_type in ['damlbmp', 'realtime']:
            zone_name = df.index[i]
            zone_id = qutil.lookup_value_in_table('zone_id_with_iso_zone_name', zone_name)
            i_record.insert(0, zone_id)
            i_record.insert(0, date_id)
            records.append(tuple(i_record))
        else:
            raise ValueError(data_type + ' has not been coded yet for inserting into table')

    return records


if __name__ == '__main__':
    load_data('2000-01-01', '2020-05-07', ['realtime'])
