import os
import urllib.parse
import pymysql

def connect_db():
    database_url = os.environ.get('JAWSDB_URL')

    if database_url:
        url = urllib.parse.urlparse(database_url)
        db_name = url.path[1:]
        db_user = url.username
        db_password = url.password
        db_host = url.hostname
        db_port = url.port

        connection = pymysql.connect(host=db_host,
                                     port=db_port,
                                     user=db_user,
                                     password=db_password,
                                     database=db_name)
    else:
        # Fallback to local database configuration if DATABASE_URL is not set
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='1234',
                                     database='police_test')

    return connection

# def connect_db():
#     # Change the host, user, password, and database accordingly
#     connection = pymysql.connect(host='localhost',
#                                  user='root',
#                                  password='1234',
#                                  database='police_test')
#     return connection

def get_data_from_assist_test(file_name=None):
    conn = connect_db()
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            if file_name:
                sql = "SELECT * FROM assist_test WHERE name=%s"
                cursor.execute(sql, (file_name,))
            else:
                sql = "SELECT * FROM assist_test"
                cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        conn.close()
    return result

# Example usage
if __name__ == '__main__':
    data = get_data_from_assist_test()
    for row in data:
        print(row)
