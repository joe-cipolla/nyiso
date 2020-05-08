"""global variables"""


root_dir = '/Users/joecipolla/Dropbox/Reference/Project_Seldon/Data/NYISO/'

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