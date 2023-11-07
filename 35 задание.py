class User:
    __name = None
    __surname = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSurn(self, surname):
        self.__surname = surname

    def getSurn(self):
        return self.__surname


class Employee(User):

    def getFull(self):
        return self.__name + ' ' + self.__surname


emp = Employee()
emp.setName('John')
emp.setSurn('Smith')

print(emp.getName())
print(emp.getSurn())

print(emp.getFull())  # ошибка!