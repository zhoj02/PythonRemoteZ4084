#pip install mysql-connector-python
from mysql.connector import connect, Error

try:
    with connect(host="localhost", user='root', password='YourNewPassword') as conn:
        print(conn)

except Error as e:
    print(e)
