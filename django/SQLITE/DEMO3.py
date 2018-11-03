import sqlite3 as sql
conn=sql.connect("raj.db")
curs=conn.cursor()
curs.execute("create table product(id number,name text, salary real)")
print("table created")
curs.close()
conn.close()
print("thanks")