# Methods are functions that belong to class 
# They defines the behavior of objects created from the class

# All methods must have self as first parameter

class Person:
    def __init__(self, name , age):
       self.name = name
       self.age = age

    # Method accessing properties
    def get_info(self):
        return f"{self.name} is {self.age} years old"

    # Method modifying property
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday ! You are now {self.age}")



p1 = Person("Dev",20)
print(p1.get_info())
p1.celebrate_birthday()

# delete method
del Person.celebrate_birthday