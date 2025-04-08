#pip install mysql-connector-python
from mysql.connector import connect, Error

try:
    with connect(host="localhost", user='root', password='YourNewPassword') as conn:
        with conn.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            print(cursor.fetchall())

except Error as e:
    print(e)
