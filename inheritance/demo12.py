class A:
    def m1(self):
        print("m1 is class A")
class B:
    def m1(self):
        print("m1 is class B")

class C(A,B):
    def m1(self):
        super().m1()
        print("m1 is class C")
class C(B,A):
    def m1(self):#
        super().m1()
        print("m1 is class C")
c=C()
c.m1()
c.m1()