"""scrapes and archives all NYISO public data"""

import requests
import os
import shutil
import zipfile
import pandas as pd


def scrape_data(start_date, end_date, root_path, data_types):
    """
    :param start_date:
    :param end_date:
    :param root_path:
    :param data_types:
    :return:
    """

    query_date_range = pd.date_range(start=start_date, end=end_date, freq='MS')

    for data_type in data_types:

        data_dir = root_path + data_type + '/'

        for query_date in query_date_range:

            # download archived zip files
            tag = str(query_date.year) + str(query_date.month).zfill(2) + '01' + data_type + '_zone_csv.zip'

            url = 'http://mis.nyiso.com/public/csv/' + data_type + '/' + tag
            my_file = requests.get(url)
            open(data_dir + tag, 'wb').write(my_file.content)
            print('downloaded ' + tag)

            # unzip each file
            with zipfile.ZipFile(data_dir + tag, 'r') as zip_ref:
                zip_ref.extractall(data_dir + tag)
            print('unzipped ' + tag)

            # delete zip file
            if os.path.isfile(data_dir + tag):
                os.remove(data_dir + tag)
                print('deleted ' + tag)

            # move files from zip directories to data_type directory
            tag = tag[:-3]
            dir_ = root_path + data_type + '/' + tag + '/'
            if os.path.isdir(dir_):
                for file_ in os.listdir(dir_):
                    os.rename(dir_ + file_, root_path + data_type + '/' + file_.split('/')[-1])
                shutil.rmtree(dir_)
                print('archived ' + tag)


if __name__ == '__main__':
    scrape_data(start_date='2020-01-01', end_date='2021-01-01',
                root_path='/Users/joecipolla/Dropbox/Reference/Project_Seldon/Data/NYISO/',
                data_types=['realtime', 'damlbmp'])
