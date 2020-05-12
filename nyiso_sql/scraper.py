"""scrapes and archives all NYISO public data"""

import requests
import os
import zipfile
import pandas as pd
import nyiso_sql.global_vars as gvars


def scrape_data(start_date, end_date, root_path, data_types):
    """
    :param start_date:
    :param end_date:
    :param root_path:
    :param data_types:
    :return:
    """

    if data_types is None:
        data_types = list(gvars.url_file_name_map.keys())

    for data_type in data_types:

        data_dir = root_path + data_type + '/'
        data_file_name = gvars.url_file_name_map[data_type][0]
        data_file_type = gvars.url_file_name_map[data_type][2]
        url_tag = gvars.url_file_name_map[data_type][3]

        if pd.to_datetime(start_date) < pd.to_datetime(gvars.url_file_name_map[data_type][1]):
            start_date = gvars.url_file_name_map[data_type][1]
        query_date_range = pd.date_range(start=start_date, end=end_date, freq='MS')

        for query_date in query_date_range:

            # download archived zip files
            if data_type == 'capacityreport':
                tag = str(query_date.year) + str(query_date.month).zfill(2) + '01' + data_file_name + '.zip'
                url = 'http://mis.nyiso.com/public/htm/' + data_type + '/zip/' + tag
            else:
                tag = str(query_date.year) + str(query_date.month).zfill(2) + '01' \
                      + data_file_name + '_' + data_file_type + '.zip'
                url = 'http://mis.nyiso.com/public/' + data_file_type + '/' + data_type + '/' + url_tag + tag
            my_file = requests.get(url)
            open(data_dir + tag, 'wb').write(my_file.content)
            print('downloaded ' + tag)

            # unzip each file
            with zipfile.ZipFile(data_dir + tag, 'r') as zip_ref:
                zip_ref.extractall(data_dir)
            print('unzipped ' + tag)

            # delete zip file
            if os.path.isfile(data_dir + tag):
                os.remove(data_dir + tag)
                print('deleted ' + tag)


if __name__ == '__main__':
    scrape_data(start_date='2000-01-01', end_date='2020-05-11',
                root_path=gvars.root_dir,
                data_types=['rtlbmp'])
