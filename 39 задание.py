class User:

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Employee(User):

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary


class Programmer(Employee):

    def set_skill(self, skill):
        self.skill = skill

    def get_skill(self):
        return self.skill


class Designer(Employee):

    def set_creativity(self, creativity):
        self.creativity = creativity

    def get_creativity(self):
        return self.creativity


programmer = Programmer()
programmer.set_name("John")
programmer.set_salary(1000)
programmer.set_skill(10)

print(programmer.get_name())
print(programmer.get_salary())
print(programmer.get_skill())