import sqlite3 as sql
conn=sql.connect("raj.db")
curs=conn.cursor()
try:
    curs.execute("insert into  product values(101,'raj',120000)")
    print("product inserted")

except sql.OperationalError as oe:
    print(oe)
finally:
    curs.close()
    conn.commit()
    conn.close()
print("thanks")
