"""sql worker functions and queries"""

import psycopg2
import nyiso_sql.global_vars as gvars


conn_closed_msg = "PostgreSQL connection is close."


def insert_row(table_name, record, conn=None, pkey_id=None, cur=None):
    """ inserts single row into table
    :param table_name - string
    :param record - list of tuples
    :param conn - db connection
    :param pkey_id - primary key
    :param cur - db cursor
    """

    sql = gvars.sql_insert_map[table_name]

    try:
        conn = psycopg2.connect(host=gvars.t_host, port=gvars.t_port, dbname=gvars.t_dbname,
                                user=gvars.t_user, password=gvars.t_pw)
        cur = conn.cursor()
        cur.execute(sql, record)
        pkey_id = cur.fetchone()[0]
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print(conn_closed_msg)

    return pkey_id


def bulk_insert_rows(table_name, records, conn=None, cur=None):
    """drops all rows from table matching row_ids
    :param table_name - string
    :param records - list of tuples, each with length = number of columns in table
    :param conn - db connection
    :param cur - db cursor
    """

    sql = gvars.sql_insert_map[table_name]

    try:
        conn = psycopg2.connect(host=gvars.t_host, port=gvars.t_port, dbname=gvars.t_dbname,
                                user=gvars.t_user, password=gvars.t_pw)
        cur = conn.cursor()
        cur.executemany(sql, records)
        conn.commit()
        print(cur.rowcount, "Record inserted successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print(conn_closed_msg)


def drop_row(table_name, row_id, conn=None, cur=None):
    """drops all rows from table matching row_ids
    :param table_name - string
    :param row_id - int
    :param conn - db connection
    :param cur - db cursor
    """

    sql = gvars.sql_drop_map[table_name]
    
    try:
        conn = psycopg2.connect(host=gvars.t_host, port=gvars.t_port, dbname=gvars.t_dbname,
                                user=gvars.t_user, password=gvars.t_pw)
        cur = conn.cursor()
        cur.execute(sql, (row_id, ))
        conn.commit()
        print(cur.rowcount, "Record deleted successfully.")
    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print(conn_closed_msg)


def bulk_drop_rows(table_name, row_ids, conn=None, cur=None):
    """drops all rows from table matching row_ids
    :param table_name - string
    :param row_ids - list of tuples
    :param conn - db connection
    :param cur - db cursor
    """

    sql = gvars.sql_drop_map[table_name]
    
    try:
        conn = psycopg2.connect(host=gvars.t_host, port=gvars.t_port, dbname=gvars.t_dbname,
                                user=gvars.t_user, password=gvars.t_pw)
        cur = conn.cursor()
        cur.executemany(sql, row_ids)
        conn.commit()
        print(cur.rowcount, "Record deleted successfully.")
    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print(conn_closed_msg)
   

if __name__ == '__main__':
    insert_row(
        'da_lmp',
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    )
    
    bulk_insert_rows(
        'da_lmp',
        [(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
          0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01),
         (1, 1, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50,
          0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50),
         (1, 1, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
          100, 100, 100, 100, 100, 100, 100, 100, 100, 100)]
    )

    drop_row('da_lmp', 13)
    bulk_drop_rows('da_lmp', [(2, ), (3, ), (4, ), (5, )])
