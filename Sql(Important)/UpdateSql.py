import sqlite3

connection = sqlite3.connect('Database_file.db')

c = connection.cursor()

c.execute("UPDATE record SET name ='John' where age==2")

connection.commit()
connection.close()

# Now Run sqlfetch.py to see the updated record