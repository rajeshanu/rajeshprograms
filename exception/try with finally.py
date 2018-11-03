import sqlite3 as sql
conn=sql.connect("sathya.db")
curs=conn.cursor()
try:
    curs.execute("insert into the employee value (102)")
except sql.OperationalError as oe:
    print(oe)
finally:
    curs.close()
    conn.close()
    print("close all connections")
print("thanks")
