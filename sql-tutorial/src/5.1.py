import sqlite3

db_path = 'C:/sql-tutorial/db/penguins-python5.db'
connection = sqlite3.connect(db_path)
cursor = connection.execute("select count(*) from penguins;")
rows = cursor.fetchall()
print(rows)