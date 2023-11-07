class User:

  def __private(self):
    print("Приватный метод")

class Employee(User):

  def test(self):
    self.__private() # Ошибка! Это связано с тем, что приватные методы не наследуются в Python.

emp = Employee()
emp.test()