#using string iter
name=input("enter the name:")
i=iter(name)
while True:
    try:
        print(next(i),end="")
    except StopIteration as si:
        break
