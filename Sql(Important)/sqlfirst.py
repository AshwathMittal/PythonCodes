'''
Sqllite3 is a pre-installed database library in python

'''

import sqlite3 #Import

conn = sqlite3.connect("Database_file.db") #Establish connection to the database file

c = conn.cursor() # Creating cursor class, For executing sql queries

# call execute method for running sql queries
c.execute("CREATE TABLE if not exists record(name text,age int)")

# Inserting data

c.execute("insert into record values ('Ashwath', 15)")

'''
To Insert Multiple Records
'''
data = [('Name1', 2), ('Name2', 3)]
for i in data:
    c.execute(f'insert into record values {i}')
conn.commit() #Save Data
conn.close() #Close Connection



'''
Fetching Data in sqlfetch.py
'''