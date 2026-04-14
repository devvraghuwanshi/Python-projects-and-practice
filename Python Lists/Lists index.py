# items in list can be accessed by index.
# positive index - 0,1,2,3,.....
# negative index - ....,-3,-2,-1 (to access items from last)
 
fruits = ["apple" , "grapes" , "Banana" , "mango"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[-1])
print(fruits[-2])

# Range of index:
# Syntax - listName[start index(inclusive) : End index(exclusive)]

print(fruits[0:3])
print(fruits[:3])
print(fruits[0:])
print(fruits[-4:-1])