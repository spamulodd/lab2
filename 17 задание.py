class Employee:

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        self.__salary = salary

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 16 or age > 70:
            raise ValueError("Недопустимый возраст")
        self.__age = age

emp = Employee("Иван", 30000, 25)

emp.set_salary(-1000) # Ошибка ValueError
emp.set_age(15) # Ошибка ValueError