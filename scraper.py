"""scrapes and archives all NYISO public data"""

import requests
import os
import shutil
import zipfile
import pandas as pd


# template -> 'data_type': ['archive_folder_name', 'oldest_available_archive_date']
url_file_name_map = {
    'realtime': ['realtime_csv', '1999-11-01'],
    'damlbmp': ['damlbmp_csv', '1999-11-01'],
    'rtasp': ['rtasp_csv', '2005-02-01'],
    'damasp': ['damasp_csv', '1999-11-01'],
    'schedlineoutages': ['SCLineOutages_csv', '2002-07-01'],
    'realtimelineoutages': ['RTLineOutages_csv', '2008-11-01'],
    'outSched': ['outSched_csv', '2001-12-01'],
    'DAMLimitingConstraints': ['DAMLimitingConstraints_csv', '2001-08-01'],
    'LimitingConstraints': ['LimitingConstraints_csv', '2002-07-01'],
    'ExternalLimitsFlows': ['ExternalLimitsFlows_csv', '2002-07-01'],
    'eriecirculationda': ['eriecirculationda_csv', '2009-05-01'],
    'eriecirculationrt': ['eriecirculationrt_csv', '2009-04-01'],
    'parSchedule': ['parSchedule_txt', '2001-08-01'],
    'parflows': ['parflows_csv', '2001-06-01'],
    'atc_ttc': ['atc_ttc_csv', '1999-11-01'],
    'ttcf': ['ttcf_csv', '2012-10-01'],
    'isolf': ['isolf_csv', '1999-11-01'],
    'zonalBidLoad': ['zonalBidLoad_csv', '2001-06-01'],
    'lfweather': ['lfweather', '2008-09-01'],
    'pal': ['pal_csv', '2001-05-01'],
    'damenergy': ['DAM_energy_rep_csv', '2000-09-01'],
    'capacityreport': ['CapacityReport', '2003-08-01'],
    'hamenergy': ['HAM_energy_rep_csv', '2000-09-01'],
    'RealTimeEvents': ['RealTimeEvents_csv', '2001-06-01'],
    'rtfuelmix': ['rtfuelmix_csv', '2015-12-01'],
    'OperMessages': ['OperMessages_csv', '2000-01-01'],
    'OpInCommit': ['OpInCommit_csv', '2019-06-01'],
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

        if pd.to_datetime(start_date) < pd.to_datetime(url_file_name_map[data_type][1]):
            start_date = url_file_name_map[data_type][1]
        query_date_range = pd.date_range(start=start_date, end=end_date, freq='MS')

        for query_date in query_date_range:

            # download archived zip files
            tag = str(query_date.year) + str(query_date.month).zfill(2) + '01' + data_file_name + '.zip'

            url = 'http://mis.nyiso.com/public/csv/' + data_type + '/' + tag
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
    scrape_data(start_date='2002-07-01', end_date='2020-05-01',
                root_path='/Users/joecipolla/Dropbox/Reference/Project_Seldon/Data/NYISO/',
                data_types=['realtime', 'damlbmp', 'rtasp', 'damasp', ])  # ['realtime', 'damlbmp']
