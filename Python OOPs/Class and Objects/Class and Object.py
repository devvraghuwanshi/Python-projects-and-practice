# CLASS:

class Car:
# Constructor: Uses __init__() method.
    # __init__() method: All classes have build-in __init__() method.
    # __init__() is always executed when class is being initialzed.
    # __init__() is Used to assign values to object properties or to perform operation when the object is being created .
    # __init__() can have default values.
    # __init__() can have multiple values.
     
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    # Self parameter : is reference to the current instance of the class.
    # it is used to access properties and methods that belongs to class.


#Methods:
    # Accessing properties with self
    def drive(self):
        print(f"You drive the car {self.model}")

    def stop(self):
        print(f"You stop the car {self.model}")

    def describe(self):
        print(f"{self.model} {self.color} {self.year}")





# OBJECTS:
Car1 = Car("Mustang",2024,"Black",False)
Car2 = Car("BMW",2025,"Grey",True)

# Accessing values 
print(Car1.model)
print(Car2.model)

# Calling methods
Car1.describe()
Car2.describe()