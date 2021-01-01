import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Как я начал учить Flask', 'Контент для первого поста')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Как я решился пройти курс от Stepik.Academy', 'Контент для второго поста')
            )

connection.commit()
connection.close()