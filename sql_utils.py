import psycopg2

# database connection parameters
t_host = 'localhost'
t_port = '5432'
t_dbname = 'seldon'
t_user = 'admin'
t_pw = 'admin'


sql_insert_map = {
    'da_lmp': '''INSERT INTO da_lmp (date_id, zone_id, he01, he02, he03, he04, he05, he06, he07, he08, he09, he10,
         he11, he12, he13, he14, he15, he16, he17, he18, he19, he20, he21, he22, he23, he24)
         VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
         RETURNING id;'''
}

sql_drop_map = {
    'da_lmp': '''DELETE FROM da_lmp WHERE id = %s;'''
}

conn_closed_msg = "PostgreSQL connnection is close."


def insert_row(table_name, records, conn=None, pkey_id=None):
    """ insert a new date into the da_lmp table """
    sql = sql_insert_map[table_name]

    try:
        conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
        cur = conn.cursor()
        cur.execute(sql, records)
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


def bulk_insert_rows(table_name, records, conn=None):

    sql = sql_insert_map[table_name]

    try:
        conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
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


def drop_row(table_name, row_id, conn=None):
    
    sql = sql_drop_map[table_name]
    
    try:
        conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
        cur = conn.cursor()
        cur.execute(sql, (row_id, ))
        conn.commit()
        print(cur.rowcount, "Record deleted successfuly.")
    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print(conn_closed_msg)


def bulk_drop_rows(table_name, row_ids, conn=None):
    """drops all rows from table matching row_ids
    :param table_name - string
    :param row_ids - list of tuples
    :param conn 
    """

    sql = sql_drop_map[table_name]
    
    try:
        conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
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
