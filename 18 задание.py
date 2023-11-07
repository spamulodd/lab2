class Employee:

  def set_age(self, age):
    if 0 < age < 120:
      self.__age = age
    else:
      raise ValueError("Возраст должен быть от 0 до 120")

  def get_salary(self):
    return str(self.__salary) + "$"

emp = Employee()

emp.set_age(150) # ValueError

print(emp.get_salary()) # 50000$