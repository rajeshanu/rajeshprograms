no=5
for x in range(1,6):
    for y in range(1,x+1):
        print(no,end="")
        if no==40:
            no=40
            print(no,end="")
            no=no+5
        else:
            num=no+5
    print()