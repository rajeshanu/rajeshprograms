class A:
    def m1(self):
        print("A class m1 method")
class B(A):
    def m2(self):
        print("B class m2 method")
    def m1(self):
        super().m1()
        print("B class m2 method")
class C(B) :
    def m3(self):
        print("C class m3 method")
b=B()
b.m2()
b.m1()
c=C()
c.m3()
c.m2()