class A:
    def assign(self,id,na):
        self.idno=id
        self.name=na
class B(A):
    def display(self):
     print(idno=self.idno)
    # print("name=self.name")
b=B()
b.assign(101,"raj")
b.display()