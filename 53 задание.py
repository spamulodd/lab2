from math import pi

class Circle:

  def __init__(self, radius):
    self.__radius = radius

  def get_area(self):
    return pi * self.__radius ** 2

  def get_circumference(self):
    return 2 * pi * self.__radius

circle = Circle(5)

print(circle.get_area())
print(circle.get_circumference())