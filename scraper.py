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

    for data_type in data_types:

        # download archived zip files
        y = 2000
        while y < 2020:
            m = 1
            while m < 13:
                tag = str(y) + str(m).zfill(2) + '01' + data_type + '_zone_csv.zip'
                url = 'http://mis.nyiso.com/public/csv/' + data_type + '/' + tag
                my_file = requests.get(url)
                open(root_path + data_type + '/' + tag, 'wb').write(my_file.content)
                print('downloaded ' + tag)
                m += 1
            y += 1

        # unzip each file
        y = 2000
        while y < 2020:
            m = 1
            while m < 13:
                tag = str(y) + str(m).zfill(2) + '01' + data_type + '_zone_csv.zip'
                with zipfile.ZipFile(root_path + data_type + '/' + tag, 'r') as zip_ref:
                    zip_ref.extractall(root_path + data_type + '/' + tag)
                print('unzipped ' + tag)
                m += 1
            y += 1

        # delete zip files
        y = 2000
        while y < 2020:
            m = 1
            while m < 13:
                tag = str(y) + str(m).zfill(2) + '01' + data_type + '_zone_csv.zip'
                file_path = root_path + data_type + '/' + tag
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(tag)
                m += 1
            y += 1

        # move files from zip directories to data_type directory
        y = 2001
        while y < 2020:
            m = 1
            while m < 13:
                tag = str(y) + str(m).zfill(2) + '01' + data_type + '_zone_csv'
                dir_ = root_path + data_type + '/' + tag + '/'
                if os.path.isdir(dir_):
                    for file_ in os.listdir(dir_):
                        os.rename(dir_ + file_, root_path + data_type + '/' + file_.split('/')[-1])
                    shutil.rmtree(dir_)
                    print(tag)
                m += 1
            y += 1


if __name__ == '__main__':
    scrape_data(start_date='2020-01-01', end_date='2021-01-01',
                root_path='/Users/joecipolla/Dropbox/Reference/Project_Seldon/Data/NYISO/',
                data_types=['realtime', 'damlbmp'])
