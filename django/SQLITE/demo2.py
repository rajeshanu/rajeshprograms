import sqlite3 as sql
conn=sql.connect(r"c:\Users\Rajesh\desktop\rajdb")
print(conn)
conn.close()
