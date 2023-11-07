class Car:
color = "Silver"
fuel = 97
brand = "Kia"
model = "Rio"
year = "2018"
driver = "Aleksander"

def go(self):
pass

def turn(self):
pass

def stop(self):
pass

def show_info(self):
print(Car.color,Car.fuel,Car.brand,Car.model,Car.year,Car.driver)
class Driver:
name="Aleksander"
surname="Moskin"
age="17"
def show_info(self):
print(Driver.name,Driver.surname,Driver.age)

myCar = Car()
myCar.go()

myCar.show_info()

myDriver = Driver()
myDriver.show_info()