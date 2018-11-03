try:
    no1=int(input("1st no:"))
    no2=int(input("2nd no:"))
    print("sum=",no1+no2)
    print("div=",no1/no2)
except ValueError:
    print("invalid input")
except ZeroDivisionError as zd:
    print(zd)
else:
    print("mul=",no1*no2)
    print("sub=",no1-no2)
    print("thanks")