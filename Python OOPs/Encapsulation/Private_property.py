# Encapsulation : Encapsulation is a process of bundling data and protecting data inside a class.
#                 It means keeping data(properties) and method together in a class , while controlling 
#                 how the data can be accessed from outside the class.


# Private Property: you can make properties private by using a double underscore __ prefix
class Person:

    def __init__(self,name,age):
        self.name = name
        self.__age = age        # Private Property

    def get_age(self):          # Getter Method
        return self.__age

    def set_age(self, age):     # Setter Method
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

# Private properties cannot be accessed directly from outside the class.
person_1 = Person("Dev",21)
print(person_1.name)
#print(person_1.__age) # This will cause an error as age is private property.


# Accessing Private Property : Use a Getter method to access a private property.
print(person_1.get_age())

# Set Private property value : Use Setter method to change private property
person_1.set_age(22)
print(person_1.get_age())