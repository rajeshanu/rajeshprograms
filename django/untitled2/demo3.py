no =int(input("enter number:"))
m=(2*no)
for x in range(0,no):
    for y in range(0, m):
        print(end=" ")
    m=m-1#decrementing m after each loop
    for y in range(0, x+1):
        print("*", end=' ')
    print(" ")
