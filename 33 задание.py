class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Employee(User):

    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname)
        self.age = age
        self.salary = salary

    def get_age(self):
        return self.age

    def get_salary(self):
        return self.salary


emp = Employee("Иван", "Петров", 25, 50000)
print(emp.get_age())
print(emp.get_salary())