from mysql.connector import connect

with open("heslo.txt", "r") as file:
    password = file.read()

jmeno_filmu = "Forrest Gump'; DROP TABLE movies; -- "

with connect(user="root", password=password, database="online_movie_rating") as conn:
    cursor = conn.cursor()

    cursor.execute(f"""
        SELECT * FROM movies WHERE title = '{jmeno_filmu}'
        """)
    print(cursor.fetchall())