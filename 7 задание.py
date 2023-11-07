class Employee:
    name = None
    salary = None
    def show(self,name,salary):
        print(self.name)
        print(self.salary)
employe = Employee()
employe.salary = 18000
employe.name = 'Shinarien'
print(employe.show())