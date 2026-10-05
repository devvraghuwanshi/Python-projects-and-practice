# Prevents user from creating an object of that class.
# Compels a user to override abstract method in child class.

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation


# Importing abstract class and  abstract method:
from abc import ABC , abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
         pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
         print("You stopped the car")

class Motorcycle(Vehicle):
    def go(self):
            print("You drive the motorcycle")

    def stop(self):
             print("You stopped the Motorcycle")
     

# Vehicle is now abstract class and we cannot give it physical form.
# vehicle = vehicle() 

car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()

