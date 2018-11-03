rows = input("Enter number of rows ")
rows = int (rows)
for x in range (rows,0,-1):
    for j in range(0, x ):
        print("*", end=' ')
    print()