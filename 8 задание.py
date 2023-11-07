class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def get_first_char(self, string):
        return string[0].upper()
    def get_initials(self):
        return self.get_first_char(self.name) + '. ' + self.get_first_char(self.surname) + '.'
student = Student('john', 'doe')
print(student.get_initials())