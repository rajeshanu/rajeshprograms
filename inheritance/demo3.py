class A:
    @staticmethod
    def show():
        print("this is A static method")


class B(A):
    def display(self):
        print("this is B instance method")
A.show()
B.show()