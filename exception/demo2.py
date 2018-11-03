no1=int(input("1st no:"))
no2=int(input("2nd no:"))
print("the sum=",no1+no2)
try:
    print("the div=",no1/no2)
except ZeroDivisionError:
    print("Invalid 2nd input")
    print("the sub=",no1-no2)
    print("the mul=",no1*no2)
    print("thanks")
