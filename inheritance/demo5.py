class A:
 def __init__(self):
     print("defult constuctor")
class B(A):
    def show(self):
        print("show of class B")
b=B()
b.show()

