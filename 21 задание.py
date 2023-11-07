class User:
    pass

user = User()
# Задание 1
print(isinstance(user, User)) # True
print(isinstance(user, int)) # False

# Задание 2

class Student:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, name):
        self.name = name

users = [
Student('user1'),
Employee('user2'),
Student('user3'),
Employee('user4'),
Student('user5'),
Employee('user6'),
Student('user7')
]

for obj in users:
    if isinstance(obj, Employee):
        print(obj.name)