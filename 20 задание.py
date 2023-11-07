class Employee:

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def get_salary(self):
        return str(self.__salary) + "$"

    def set_age(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            raise ValueError("Возраст должен быть от 0 до 120")

emp = Employee("Иван", 50000, 35)

print(emp.get_salary()) # 50000$

emp.set_age(50) # ошибка ValueError