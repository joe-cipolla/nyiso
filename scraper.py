"""scrapes and archives all NYISO public data"""

import requests
import os
import zipfile
import pandas as pd


url_file_name_map = {
    # 'data_type': ['archive_folder_name', 'oldest_available_archive_date', 'file_type', 'url_tag']
    'realtime': ['realtime_zone', '1999-11-01', 'csv', ''],
    'damlbmp': ['damlbmp_zone', '1999-11-01', 'csv', ''],
    'rtasp': ['rtasp', '2005-02-01', 'csv', ''],
    'damasp': ['damasp', '1999-11-01', 'csv', ''],
    'schedlineoutages': ['SCLineOutages', '2002-07-01', 'csv', ''],
    'realtimelineoutages': ['RTLineOutages', '2008-11-01', 'csv', ''],
    'outSched': ['outSched', '2001-12-01', 'csv', ''],
    'DAMLimitingConstraints': ['DAMLimitingConstraints', '2001-08-01', 'csv', ''],
    'LimitingConstraints': ['LimitingConstraints', '2002-07-01', 'csv', ''],
    'ExternalLimitsFlows': ['ExternalLimitsFlows', '2002-07-01', 'csv', ''],
    'eriecirculationda': ['ErieCirculationDA', '2009-05-01', 'csv', ''],
    'eriecirculationrt': ['ErieCirculationRT', '2009-04-01', 'csv', ''],
    'parSchedule': ['parSchedule', '2001-08-01', 'txt', ''],
    'ParFlows': ['ParFlows', '2001-06-01', 'csv', ''],
    'atc_ttc': ['atc_ttc', '1999-11-01', 'csv', ''],
    'ttcf': ['ttcf', '2014-10-01', 'csv', 'zip/'],
    'isolf': ['isolf', '1999-11-01', 'csv', ''],
    'zonalBidLoad': ['zonalBidLoad', '2001-06-01', 'csv', ''],
    'lfweather': ['lfweather', '2008-09-01', 'csv', ''],
    'pal': ['pal', '2001-05-01', 'csv', ''],
    'damenergy': ['DAM_energy_rep', '2000-09-01', 'csv', ''],
    'capacityreport': ['CapacityReport', '2003-08-01', 'htm', ''],
    'hamenergy': ['HAM_energy_rep', '2000-09-01', 'csv', ''],
    'RealTimeEvents': ['RealTimeEvents', '2001-06-01', 'csv', ''],
    'rtfuelmix': ['rtfuelmix', '2015-12-01', 'csv', ''],
    'OperMessages': ['OperMessages', '2000-01-01', 'csv', ''],
    'OpInCommit': ['OpInCommit', '2019-06-01', 'csv', ''],
}


def scrape_data(start_date, end_date, root_path, data_types):
    """
    :param start_date:
    :param end_date:
    :param root_path:
    :param data_types:
    :return:
    """

    for data_type in data_types:

        data_dir = root_path + data_type + '/'
        data_file_name = url_file_name_map[data_type][0]
        data_file_type = url_file_name_map[data_type][2]
        url_tag = url_file_name_map[data_type][3]

        if pd.to_datetime(start_date) < pd.to_datetime(url_file_name_map[data_type][1]):
            start_date = url_file_name_map[data_type][1]
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
    scrape_data(start_date='2002-01-01', end_date='2020-05-01',
                root_path='/Users/joecipolla/Dropbox/Reference/Project_Seldon/Data/NYISO/',
                data_types=['rtfuelmix', 'OperMessages', 'OpInCommit'])
