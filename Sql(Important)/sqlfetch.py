import sqlite3

connection = sqlite3.connect('Database_file.db')

c = connection.cursor()
c.execute("SELECT * FROM record")
d = c.fetchall()
print(d)
# OR
for i in d:
    print(i)
connection.close()