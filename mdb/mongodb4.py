from pymongo import MongoClient
curs=MongoClient().simha.student.find()

if curs.count()>0:
    for x in curs:
        print(x)
else:
        print("No Data found")