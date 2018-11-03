class employee():
    def assign (self,id=0,name=None,sal=00):
        self.idno=id
        self.name=name
        self.salary=sal
    def display(self):
          print("id=",self.idno)
          print("name=",self.name)
          print("sal=",self.salary)
e=employee()
e.assign()
e.display()
e1=employee()
e1.assign(101,'raj')
e1.display()
e2=employee()
e2.assign(101,'ravi',120000.00)
e2.display()