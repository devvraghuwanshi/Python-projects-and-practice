# Lists are ordered , changable , allow duplicate values.
# Lists are used to store multiple value in single variable.

# List item datatypes - items can be of any datatype.
thisList_1 = ["apple" , "banana" , "mango"]
thisList_2 = [1,2,3,4,5]
thisList_3 = [True,False,True,False]
thisList_4 = ["abc" , 78 , True , "mango"]

print(thisList_1)
print(thisList_2)
print(thisList_3)
print(thisList_4)

# len(listName) - gives length of list.
print(len(thisList_2))

# type(listname) - list type is object
print(type(thisList_1))

# list constructor - lists can also be declared using constructor.
# syntax : listName = list(("val1" , "val2" , "val3"))

fruits = list(("apple" , "orange" , "grapes"))
print(fruits)
