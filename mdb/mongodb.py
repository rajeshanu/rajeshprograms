from pymongo import MongoClient
mc=MongoClient()
sa=mc.rajesh
d1={"id":123,"name":"raj","fee":12000}
sa.Student.insert(d1)
print("data inseted")
