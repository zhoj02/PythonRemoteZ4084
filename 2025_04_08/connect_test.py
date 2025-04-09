#pip install mysql-connector-python


from mysql.connector import connect, Error

with open("heslo.txt","r") as file:
    password = file.read()

try:
    with connect(host="localhost", user='root', password=password) as conn:
        print(conn)

except Error as e:
    print(e)
