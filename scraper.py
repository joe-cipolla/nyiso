import requests
import os
import shutil

root = '/Users/joecipolla/Dropbox/Reference/Project_Seldon/Data/NYISO/'
data_type = 'realtime'  # 'damlbmp'

# # download archived zip files
# y = 2000
# while y < 2020:
#     m = 1
#     while m < 13:
#         tag = str(y) + str(m).zfill(2) + '01' + data_type + '_zone_csv.zip'
#         url = 'http://mis.nyiso.com/public/csv/' + data_type + '/' + tag
#         myfile = requests.get(url)
#         open(root + data_type + '/' + tag, 'wb').write(myfile.content)
#         print(tag)
#         m += 1
#     y += 1


# manually unzip each file


# # delete zip files
# y = 2000
# while y < 2020:
#     m = 1
#     while m < 13:
#         tag = str(y) + str(m).zfill(2) + '01' + data_type + '_zone_csv.zip'
#         file_path = root + data_type + '/' + tag
#         if os.path.isfile(file_path):
#             os.remove(file_path)
#             print(tag)
#         m += 1
#     y += 1

# # move files from zip directories to data_type directory
# y = 2001
# while y < 2020:
#     m = 1
#     while m < 13:
#         tag = str(y) + str(m).zfill(2) + '01' + data_type + '_zone_csv'
#         dir_ = root + data_type + '/' + tag + '/'
#         if os.path.isdir(dir_):
#             for file_ in os.listdir(dir_):
#                 os.rename(dir_ + file_, root + data_type + '/' + file_.split('/')[-1])
#             shutil.rmtree(dir_)
#             print(tag)
#         m += 1
#     y += 1