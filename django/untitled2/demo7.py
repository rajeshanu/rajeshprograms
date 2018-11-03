for x in range(4):
    for y in range(1,x+1,4):
        print(end="")
    for y in range(x+1):
        print("* ",end="")
    print()
for x in range(4):
    for y in range(x+2):
        print(end="")
    for y in range(4,x+1,-1):
        print("* ",end="")
    print()