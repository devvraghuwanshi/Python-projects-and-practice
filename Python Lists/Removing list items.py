list1 = ["html" , "css" , "JS" , "BootStrap"]
print(list1)

# remove(value) - removes specified item
list1.remove("BootStrap")
print(list1)

# pop(index) - removes item at specified index.
list1.pop(1)
# list1.pop() - if do not specify it removes last element.
print(list1)

list2 = ["1" , "2" , "3" , "3"]
# del keyword - 
del list2[0] #removes element at specified index.
print(list2)

# list2 = ["Java" , "c++" , "c" ,"C#"]
# del list2    #delete the list completely.
# print(list2)

# clear() - empties the list , list remains but has no value
list3 = ["apple" , "mango"]
list3.clear()
print(list3)




