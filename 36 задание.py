class User:
  __name = ''

  def setName(self,name):
    self.__name = name

  def getName(self):
    return self.__name

class Employee(User):

  def setName(self,name):
    if len(name) > 0:
      super().setName(name)

emp = Employee()
emp.setName("John")
print(emp.getName())