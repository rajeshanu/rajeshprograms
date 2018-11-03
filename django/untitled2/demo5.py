no=int(input("enter no:"))
rows = 4
for x in range(1, rows+1):
    for y in range(1, (rows-x)+1):
        print(end="  ")
    while no != (2*x-1):
        print("* ", end="")
        no = no + 1
    no= 0
    print()