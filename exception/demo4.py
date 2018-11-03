try:
    no1=int(input("1st no:"))
    no2=int(input("2nd no:"))
    print("the sum=",no1+no2)
    try:
        print("the div=",no1/no2)
    except ZeroDivisionError as zd:
          print(zd)
          print("the mul=",no1*no2)
          print("the sub=",no1-no2)
except ValueError:
    print("only integer values")
    print("thanks")


