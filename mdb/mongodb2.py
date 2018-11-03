from pymongo import MongoClient
from pymongo import errors
mc=MongoClient()
sa=mc.simha
d1={"_id":1011,"name":"Simha","salary":120000}
try:
    sa.student.insert(d1)
    print("Data inserted")
except errors.DuplicateKeyError as dky:
    print(dky)
