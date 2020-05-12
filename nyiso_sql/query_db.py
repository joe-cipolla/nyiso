"""database query functions"""

import psycopg2
import pandas as pd
import nyiso_sql.nyiso_sql.global_vars as gvars
import nyiso_sql.nyiso_sql.gen_utils as gen_utils


default_zones = ['MHK_VL', 'CAPTIL', 'CENTRL', 'DUNWOD', 'GENESE', 'HQ', 'HUD_VL', 'LONGIL',
                 'MILLWD', 'NYC', 'NORTH', 'NPX', 'OH', 'PJM', 'WEST']


def get_da_lmp(q_dates, zones=None):
    """
    :param - q_dates, string or list of strings in YYYY-MM-DD format. If two value list, date range will be calculated
    between the two dates.
    :param - zones, string or list of strings of zones to be queried
    """

    if isinstance(q_dates, str):
        q_dates = [q_dates]
    elif not isinstance(q_dates, list):
        raise ValueError('dates must be of type list or a single string')

    # check if each date in q_dates is actually a date
    for q_date in q_dates:
        if not gen_utils.is_valid_date(q_date):
            raise ValueError(q_date + ' is not a valid date')

    # convert two value q_dates list into range of dates between each value
    if len(q_dates) == 2:
        q_dates = pd.date_range(q_dates[0], q_dates[1]).to_list()
        q_dates = [i.strftime('%Y-%m-%d') for i in q_dates]

    if zones is None:
        zones = default_zones
    elif isinstance(zones, str):
        zones = [zones]
    elif not isinstance(zones, list):
        raise ValueError('zones must be a single string or list of strings')

    sql = '''   SELECT t.date, z.zone, d.he01, d.he01, d.he02, d.he03, d.he04, d.he05, d.he06, d.he07, d.he08, 
                d.he09, d.he10, d.he11, d.he12, d.he13, d.he14, d.he15, d.he16, d.he17, d.he18, d.he19, d.he20, 
                d.he21, d.he22, d.he23, d.he24 FROM da_lmp AS d
                JOIN dim_date as t on d.date_id = t.id
                JOIN dim_zone as z on d.zone_id = z.id
                WHERE t.date in %s
                AND z.zone in %s '''
    conn = None
    try:
        conn = psycopg2.connect(host=gvars.t_host, port=gvars.t_port, dbname=gvars.t_dbname,
                                user=gvars.t_user, password=gvars.t_pw)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    df = pd.read_sql(sql, conn, params=[tuple(q_dates), tuple(zones)])

    return df


if __name__ == '__main__':
    df = get_da_lmp(['2020-05-01', '2020-05-07'], 'CAPITL')
    print(df)
