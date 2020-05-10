root_dir = '/Users/joecipolla/Dropbox/Reference/Project_Seldon/Data/NYISO/'

# database connection parameters
t_host = 'localhost'
t_port = '5432'
t_dbname = 'seldon'
t_user = 'admin'
t_pw = 'admin'

url_file_name_map = {
    # 'data_type': ['archive_folder_name', 'oldest_available_archive_date', 'file_type', 'url_tag',
    # 'file_tag', 'table_name']
    'realtime': ['realtime_zone', '1999-11-01', 'csv', '', '_zone', 'rt_lmp'],
    'damlbmp': ['damlbmp_zone', '1999-11-01', 'csv', '', '_zone', 'da_lmp'],
    'rtasp': ['rtasp', '2005-02-01', 'csv', '', '', 'rt_asp'],
    'damasp': ['damasp', '1999-11-01', 'csv', '', '', 'da_asp'],
    'schedlineoutages': ['SCLineOutages', '2002-07-01', 'csv', '', '', 'tbd'],
    'realtimelineoutages': ['RTLineOutages', '2008-11-01', 'csv', '', '', 'tbd'],
    'outSched': ['outSched', '2001-12-01', 'csv', '', '', 'tbd'],
    'DAMLimitingConstraints': ['DAMLimitingConstraints', '2001-08-01', 'csv', '', '', 'tbd'],
    'LimitingConstraints': ['LimitingConstraints', '2002-07-01', 'csv', '', '', 'tbd'],
    'ExternalLimitsFlows': ['ExternalLimitsFlows', '2002-07-01', 'csv', '', '', 'tbd'],
    'eriecirculationda': ['ErieCirculationDA', '2009-05-01', 'csv', '', '', 'tbd'],
    'eriecirculationrt': ['ErieCirculationRT', '2009-04-01', 'csv', '', '', 'tbd'],
    'parSchedule': ['parSchedule', '2001-08-01', 'txt', '', '', 'tbd'],
    'ParFlows': ['ParFlows', '2001-06-01', 'csv', '', '', 'tbd'],
    'atc_ttc': ['atc_ttc', '1999-11-01', 'csv', '', '', 'tbd'],
    'ttcf': ['ttcf', '2014-10-01', 'csv', 'zip/', 'tbd'],
    'isolf': ['isolf', '1999-11-01', 'csv', '', '', 'tbd'],
    'zonalBidLoad': ['zonalBidLoad', '2001-06-01', 'csv', '', '', 'tbd'],
    'lfweather': ['lfweather', '2008-09-01', 'csv', '', '', 'tbd'],
    'pal': ['pal', '2001-05-01', 'csv', '', '', 'tbd'],
    'damenergy': ['DAM_energy_rep', '2000-09-01', 'csv', '', '', 'tbd'],
    'capacityreport': ['CapacityReport', '2003-08-01', 'htm', '', '', 'tbd'],
    'hamenergy': ['HAM_energy_rep', '2000-09-01', 'csv', '', '', 'tbd'],
    'RealTimeEvents': ['RealTimeEvents', '2001-06-01', 'csv', '', '', 'tbd'],
    'rtfuelmix': ['rtfuelmix', '2015-12-01', 'csv', '', '', 'tbd'],
    'OperMessages': ['OperMessages', '2000-01-01', 'csv', '', '', 'tbd'],
    'OpInCommit': ['OpInCommit', '2019-06-01', 'csv', '', '', 'tbd'],
}

sql_insert_map = {
    'da_lmp': '''INSERT INTO da_lmp (date_id, zone_id, he01, he02, he03, he04, he05, he06, he07, he08, he09, he10,
                 he11, he12, he13, he14, he15, he16, he17, he18, he19, he20, he21, he22, he23, he24)
                 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
                 RETURNING id;''',
    'dim_date': '''INSERT INTO dim_date (date, weekday_id, month_id, year_id, season_id, quarter_id) 
                   VALUES(%s,%s,%s,%s,%s,%s)'''
}

sql_drop_map = {
    'da_lmp': '''DELETE FROM da_lmp WHERE id = %s;'''
}

sql_lookup_map = {
    'zone_name':                    """SELECT zone FROM dim_zone WHERE id = %s""",
    'zone_id_with_zone_name':       """SELECT id FROM dim_zone WHERE zone = %s""",
    'zone_id_with_iso_zone_name':   """SELECT id FROM dim_zone WHERE iso_zone_name = %s""",
    'iso_id_with_zone_name':        """SELECT iso_id FROM dim_zone WHERE zone = %s""",
    'iso_name':                     """SELECT iso FROM dim_iso WHERE id = %s""",
    'date_id':                      """SELECT id FROM dim_date WHERE date = %s""",
    'weekday_id':                   """SELECT id FROM dim_weekday WHERE weekday = %s""",
    'month_id':                     """SELECT id FROM dim_month WHERE month = %s""",
    'year_id':                      """SELECT year_id FROM dim_year WHERE year = %s""",
    'season_id':                    """SELECT season_id FROM dim_month WHERE month = %s""",
    'quarter_id':                   """SELECT quarter_id FROM dim_month WHERE month = %s""",
}
