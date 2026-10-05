# Multi-level inhertance : Whem a derived(child) class inherits another derived(child) class.

# Grand parent
class Organism:

    alive = True

# Parent
class Animal(Organism):
    def eat(self):
        print("This animal is eating")

# Child
class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()       #Object of Child class
print(dog.alive)  #Calling inhertied method or class variable.
