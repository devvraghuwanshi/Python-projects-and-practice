# Method overriding: An object will use method which is more closely assosiated with itself first, before relying on method that it may inherit from parent class.

# Parent class:
class Animal:
    def eat(self):
        print("This animal is eating")

# Child class:
class Rabbit:
    def eat(self):
        print("This rabbit is eating carrot")

rabbit = Rabbit()
rabbit.eat()

# Method signature : Method_name(parameter)
# Method signature shoould be same if you want to do method overriding in child class.
