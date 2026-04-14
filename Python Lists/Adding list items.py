list1 = ["html" , "css" , "JS" , "BootStrap"]
print(list1)

# append(value) - add an item to the end of the list.
list1.append("react")
print(list1)

# insert(index,value) - inserts an item at specific index.
list1.insert(0,"python")
print(list1)

# extend(another iterable object name) - to append elements from another iterable object to current list

list2 = ["Java" , "c++" , "c" ,"C#"]
list1.extend(list2)
print(list1)

