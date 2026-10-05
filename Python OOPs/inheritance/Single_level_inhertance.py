# Inhertance : Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class : Is the class being inherited from, also called base class.
class Animal:
    alive = True

    def sleep(self):
        print("This animal is sleeping")

    def eat(self):
        print("This animal is eating")


# Child class : Is the class that inherits from another class , also called derived class.
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Tiger(Animal):
    def roar(self):
        print("Tiger is Roaring")

class Hawk(Animal):
    def fly(self):
        print("Hawk is flying")

# Objects from child classes:
dog = Dog()
tiger = Tiger()
hawk = Hawk()

# Inherited methods:
print(dog.alive)
tiger.sleep()
hawk.eat()

dog.bark()
tiger.roar()
hawk.fly()

