class A:
    def show(self):
        print("i am show of class A")
class B(A):
    def display(self):
        print( "i am display of class B")
class C(B):
    def info(self):
        print("info of  class C")
c=C()
c.info()
c.show()
c.display()