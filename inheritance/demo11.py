class A:
    def m1(self):
        print("m1 is class A")
class B:
    def m1(self):
        print("m1 is class B")

class C(A,B):
    def m2(self):
        print("m2 is class C")
c=C()
c.m1()
c.m2()

