
for x in range(4):
    for y in range(1, (4-x)+1):
        print(end="  ")
    for y in range(2*x+1):
        print("* ", end="")
    print()
