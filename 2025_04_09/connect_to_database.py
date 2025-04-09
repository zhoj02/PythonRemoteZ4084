from mysql.connector import connect

with open("heslo.txt", "r") as file:
    password = file.read()

with connect(user="root", password=password) as conn:
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    print(cursor.fetchall())
