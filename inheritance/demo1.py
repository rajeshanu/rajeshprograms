class A:
    def display(self):
        print("i am display")
class B(A):
    def show(self):
        print("this is show")
a1=A()
a1.display()
b1=B()
b1.show()
b1.display()