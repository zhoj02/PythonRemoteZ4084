from mysql.connector import connect

with open("heslo.txt", "r") as file:
    password = file.read()

with connect(user="root", password=password, database="online_movie_rating") as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE movies(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100)
        )
        """)
