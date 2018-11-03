class A:
    company_name="rajesh"
    def display(self):
        print("this is display")
class B(A):
    def show(self):
        print("this is show")
#calling static variable using class A
print(A.company_name)
#calling static variable using class B
print(B.company_name)
b1=B()
b1.show()
b1.display()


