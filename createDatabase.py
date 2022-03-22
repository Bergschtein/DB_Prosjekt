import sqlite3 as sql

con = sql.connect("KaffeDB.db")
# con = sql.connect("test.db")
cursor = con.cursor()

with open('KaffeDB.sql', 'r') as sql_file:
    con.executescript(sql_file.read())
con.close()