import psycopg2
from flask import Flask
from flask import render_template # render the error page


app = Flask(__name__)
@app.route("/")

# connect to database
t_host = 'localhost'
t_port = '5432'
t_dbname = 'seldon'
t_user = 'admin'
t_pw = 'admin'
db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
db_cursor = db_conn.cursor()


@app.route("/import")
def csv_import():

    # trap errors for opening the file
    try:
        t_path_n_file = 'data/users/csv'
        f_contents = open(t_path_n_file, 'r')
    except psycopg2.Error as e:
        t_message = 'Database error: ' + e + '/n open() text file: ' + t_path_n_file
        return render_template('error_page.html', t_message=t_message)

    # trap errors from copying the array to our database
    try:
        db_cursor.copy_from(f_contents, 'tbl_users', columns=('t_name_user', 't_email'), sep=', ')
    except psycopg2.Error as e:
        t_message = 'Database error: ' + e + '/n copy_from'
        return render_template('error_page.html', t_message=t_message)

    # it got this far: success!

    # clean up by closing the database cursor and connection
    db_cursor.close()
    db_conn.close()
