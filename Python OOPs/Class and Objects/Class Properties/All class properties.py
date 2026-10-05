# Properties are variables that belong to a class. They store data for each object created from the class.
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")
car2 = Car("BMW", "RED")
# Accessing class properties.
print(car1.brand)
print(car1.model)

# Modify class property.
car2.model = "BLACK"
print(car2.model)

# Delete Propert
# del car2.model
# print(car2.model)

# Add New Property
car1.color = "Black"
car1.year = 2026

# Modify Class property

class Person:
  lastname = ""

  def __init__(self,name):
    self.name = name

P1 = Person("Dev")

Person.lastname = "Patel"
print(Person.lastname)

