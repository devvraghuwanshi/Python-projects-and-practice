# Creating classes:
class Car:
    color = None

class Bike:
    color = None

# Function with object as argument:
def change_color(vehicle,color):
    vehicle.color = color

# Creating Objects:
car_1 = Car()
car_2 = Car()
car_3 = Car()
bike_1 = Bike()

# Calling function with object as parameter
change_color(car_1,"Black")
change_color(car_2,"Red")
change_color(car_3,"Yellow")
change_color(bike_1,"white")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)