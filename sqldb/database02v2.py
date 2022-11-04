#!/usr/bin/env python3

# that first line is a shebang line; it tells linux that it should use Python to run this script
# it DOES need that # in front of it, so I just put it back and now it should be good!



# add an IF NOT EXISTS on your create table line; check out step number 13 in lab 2 2
import sqlite3
conn = sqlite3.connect('challenge.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE IF NOT ExISTS thursday
 (ID INT PRIMARY KEY     NOT NULL,
 band           TEXT     NOT NULL,
 hometown       TEXT     NOT NULL,
 year           INT      NOT NULL);''')

# I was having the same error yesterday that you are having here- make sure that you end
# that long execute string with the correct syntax-- );   compare to what's in the lab

print("Table created successfully")
conn.close()
