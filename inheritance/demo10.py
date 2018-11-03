class first:
    def calc(self,no1,no2):
        print("add",no1+no2)
        print("sub",no1-no2)
class second(first):
    def calc(self,no1,no2):
        super(second, self).calc(no1,no2)
        print("mul",no1*no2)
        print("div",no1/no2)
class third(second):
    def clac(self,no1,no2):
        super().calc(no1,no2)
        print("mod",no1%no2)
        print("flor div",no1//no2)
f1=first()
f1.calc(10,20)
s1=second()
s1.calc(20,30)
t=third()
t.calc(12,6)
