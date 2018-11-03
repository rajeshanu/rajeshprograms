from pymongo import MongoClient
mc=MongoClient()
sa=mc.rajesh
d1={"id":121,"name":"simha","fee":12000}
d2={"id":122,"name":"sanju","fee":12000}
d3={"id":123,"name":"sumath","fee":12000}
d4={"id":124,"name":"maheshf","fee":12000}
sa.Student.insert(d1)
sa.Student.insert(d2)
sa.Student.insert(d3)
sa.Student.insert(d4)
print("data inseted")
