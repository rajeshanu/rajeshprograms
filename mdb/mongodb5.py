from pymongo import MongoClient
idno=int(input("Enter Idno:"))
d1={"_id":idno}
curs=MongoClient().simha.student.find(d1)

if curs.count()>0:
    for x in curs:
        print(x)
else:
        print("Invalid Input")