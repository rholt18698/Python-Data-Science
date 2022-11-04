#!/usr/bin/env python3
# oops! deleted that "challenge.db" you had at the top of the file


import sqlite3
conn = sqlite3.connect('challenge.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE thursday
 (ID INT PRIMARY KEY     NOT NULL,
 band           TEXT     NOT NULL,
 hometown       TEXT     NOT NULL,
 year           INT      NOT NULL);''')

# I was having the same error yesterday that you are having here- make sure that you end
# that long execute string with the correct syntax-- );   compare to what's in the lab

print("Table created successfully")
conn.close()

