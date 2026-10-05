# Duck Typing : Concept where the class of the object is less important than the methods/attributes 
#               class type is not checked if minimum method/attribute are present
#               "If it walks like duck, it quacks like duck, it must be duck"

class Duck:
    def walk(self):
        print("This Duck is Walking")

    def talk(self):
        print("This duck is Qwuacking")

class Chicken:
    def walk(self):
        print("This Chicken is Walking")

    def talk(self):
        print("This chicken is clucking") 

class Person:
    def catch(self , duck):
        duck.walk()
        duck.talk()
        print("You caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)

# With the help of Duck-Typing you can also pass chicken(object) as parameter , since it has same methods and attributes

person.catch(chicken)