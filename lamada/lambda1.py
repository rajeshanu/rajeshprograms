result = lambda x , y : x + y
print(result)
print(result (10,20))
print("lamda function with 2 argument")
# lambda function with two arguments
result = lambda id , name : print("ID :",id,'\nName :',name)
result(10,"raj")
# lamda function with defult values
result = lambda id = None, name = None , salary = 0.0 : print('ID :',id,'\nName :',name,'\nSalary :',salary)
print(result)
result(1d=100)