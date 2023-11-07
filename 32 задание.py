class User:

    def set_age(self, age):
        if age >= 0:
            self.age = age
        else:
            raise Exception("Возраст должен быть больше 0")

class Employee(User):

    def set_age(self, age):
        if age <= 120:
            super().set_age(age)
        else:
            raise Exception("Возраст должен быть меньше 120")