class A:
    def __init__(self):
        print("defualt constructor")
    def __del__(self):
        print("destructor of class A")
class B(A):
    def show(self):
        print("show")
b=B()
b.show()