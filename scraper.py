import requests

data_type = 'damlbmp'

y = 2000
while y < 2010:
    m = 1
    while m < 13:
        tag = str(y) + str(m).zfill(2) + '01' + data_type + '_zone_csv.zip'
        url = 'http://mis.nyiso.com/public/csv/' + data_type + '/' + tag
        myfile = requests.get(url)
        open('/Users/joecipolla/Dropbox/Reference/Project_Seldon/Data/NYISO/'
             + data_type + '/' + tag, 'wb').write(myfile.content)
        print(tag)
        m += 1
    y += 1
