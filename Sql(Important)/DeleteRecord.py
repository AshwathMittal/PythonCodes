import sqlite3

connection = sqlite3.connect('Database_file.db')

c = connection.cursor()

c.execute("DELETE from record where name=='John'")

connection.commit()
connection.close()