import sqlite3
import sys

db_path = 'C:/sql-tutorial/db/penguins-python5.db'
connection = sqlite3.connect(db_path)
cursor = connection.cursor()
cursor = cursor.execute("select species, island from penguins limit 5;")
while row := cursor.fetchone():
    print(row)