class A:
    def m1(self):
        print("class A")
class B(A):
    def m2(self):
        print("class B")
class C(B):
    def m3(selfo):
        print("class C")
a=A()
a.m1()
b=B()
b.m1()
b.m2()
c=C()
c.m1()
c.m2()
c.m3()