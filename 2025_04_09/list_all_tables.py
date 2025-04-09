from mysql.connector import connect

with open("heslo.txt", "r") as file:
    password = file.read()

with connect(user="root", password=password, database="mysql") as conn:
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    print(cursor.fetchall())
