# Class Variable : Shared among all instances of a class defined outside the constructor.
#                  Allow you to share data among all objects created from that class.

class Student:

    class_year = 2025                     #Class Property

    def __init__(self,name,age):
        self.name = name                  #instance property
        self.age = age

    

Student1 = Student("Dev",20)
print(Student1.name)
print(Student1.age)
print(Student.class_year)