d={
    "idno":101,
    "name":"raj",
    "salary":"1234512"
}
for x in d.items():
    print(x)
print("---------------------")
for x,y in d.items():
    print(x,y)
print("----unpacking tuple and assign -------")
for x in d.keys():
    print(x)
print("------------------")
for x in d. values():
    print(x)