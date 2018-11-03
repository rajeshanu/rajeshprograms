import sqlite3 as sql
conn=sql.connect("rajdb")
print(conn)
conn.close()